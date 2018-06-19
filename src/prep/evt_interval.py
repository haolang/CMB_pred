
from src.common.my_data import Data
from src.common.time_used import runtime
import pandas as pd
import time

class EvtInterval:

    def __init__(self):
        self.data = Data()

    def get_evt_times(self):

        evt_datas = pd.read_table(self.data.output.sorted_train_log)
        usr_ids = set(pd.read_table(self.data.output.sorted_train_flg)['USRID'])
        evt_names = set(evt_datas['EVT_LBL'])
        result = dict()


        for usr_id in usr_ids:
            usr_id = str(usr_id)
            times = dict()
            for evt_name in evt_names:
                evt_name = str(evt_name)
                times[evt_name] = ''
                result[usr_id] = times

        for usr_id_log, evt_log, occ_tim in zip(evt_datas['USRID'], evt_datas['EVT_LBL'], evt_datas['OCC_TIM']):
            usr_id_log = str(usr_id_log)
            evt_log = str(evt_log)
            if result[usr_id_log][evt_log] == '':
                result[usr_id_log][evt_log] += occ_tim
            else:
                result[usr_id_log][evt_log] += "|" + occ_tim

        result_csv = []
        for k, v in result.items():  # k > id
            k = str(k)
            times = dict()
            times['USRID'] = k
            for k1, v1 in v.items():  # k1 > evt_name
                if v1 == '':
                    times[k1] = 0
                else:
                    occ_time = v1.split('|')
                    # print(occ_time)
                    for occ_time_item, i in zip(occ_time, range(0, len(occ_time))):
                        time_array = time.strptime(occ_time_item, "%Y-%m-%d %H:%M:%S")
                        time_stamp = int(time.mktime(time_array))
                        occ_time[i] = time_stamp

                    times[k1] = max(occ_time) - min(occ_time)  # 事件间隔
            result_csv.append(times)

        data = pd.DataFrame(result_csv)
        data.to_csv(self.data.output.prep_evt_interval, index=False, sep='\t')


if __name__ == "__main__":
    runtime.start()
    evt_interval = EvtInterval()
    evt_interval.get_evt_times()
    runtime.end()
