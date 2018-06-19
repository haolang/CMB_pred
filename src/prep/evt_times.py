
from src.common.my_data import Data
from src.common.time_used import runtime
import pandas as pd

class EvtTimes:

    def __init__(self):
        self.data = Data()

    def get_evt_times(self):

        evt_datas = pd.read_table(self.data.output.sorted_train_log)
        usr_ids = set(pd.read_table(self.data.output.sorted_train_flg)['USRID'])
        # usr_id_log = set(evt_datas['USRID'])  # log 存在的usrid
        evt_names = set(evt_datas['EVT_LBL'])
        # print(len(evt_names), evt_names)
        result = dict()

        for usr_id in usr_ids:
            usr_id = str(usr_id)
            times = dict()
            for evt_name in evt_names:
                evt_name = str(evt_name)
                times[evt_name] = 0
                result[usr_id] = times

        for usr_id_log, evt_log in zip(evt_datas['USRID'], evt_datas['EVT_LBL']):
            usr_id_log = str(usr_id_log)
            evt_log = str(evt_log)
            result[usr_id_log][evt_log] += 1

        result_csv = []
        for k, v in result.items():  # k > id
            k = str(k)
            times = dict()
            times['USRID'] = k
            for k1, v1 in v.items():  # k1 > evt_name
                times[k1] = v1
            result_csv.append(times)


        # result['USRID'] = usr_ids
        # result['EVT_LBL'] = evt_datas['EVT_LBL']

        # result = np.zeros((len(evt_names), len(usr_ids)))
        # for usr_id, i in zip(usr_ids, range(0, len(usr_ids))):
        #     # 如果log文件中没有记录则不作统计，所有事件的频次设置为0
        #     if usr_id in usr_id_log:
        #         for evt_name, j in zip(evt_names, range(0, len(evt_names))):
        #             evt_times = 0
        #             for evt, id in zip(evt_datas['EVT_LBL'], evt_datas['USRID']):
        #                 if evt_name == evt:
        #                     evt_times += 1
        #                     if id != usr_id:  # 一旦同一id统计完毕跳出循环
        #                         break
        #             result[i][j] = evt_times

        data = pd.DataFrame(result_csv)
        data.to_csv(self.data.output.prep_evt_times, index=False, sep='\t')
        # print(result_csv)


if __name__ == "__main__":
    runtime.start()
    evt_times = EvtTimes()
    evt_times.get_evt_times()
    runtime.end()
