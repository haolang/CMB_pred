
from src.common.my_data import Data
from src.common.time_used import runtime
import pandas as pd
# import time


class UsrEvtTestCSV:

    def __init__(self):
        self.data = Data()

    def get_evt_times(self):

        evt_datas = pd.read_table(self.data.output.sorted_test_log)
        usr_ids = set(pd.read_table(self.data.output.sorted_test_agg)['USRID'])
        # evt_names = set(evt_datas['EVT_LBL'])
        result = dict()

        for usr_id in usr_ids:
            usr_id = str(usr_id)
            result[usr_id] = ''

        for usr_id_log, evt_log in zip(evt_datas['USRID'], evt_datas['EVT_LBL']):
            usr_id_log = str(usr_id_log)
            evt_log = str(evt_log)
            if result[usr_id_log] == '':
                result[usr_id_log] += evt_log
            else:
                result[usr_id_log] += " " + evt_log

        result_csv = []

        for k, v in result.items():  # k > id
            # k = str(k)
            # result_csv['USRID'] = k
            row = dict()
            if v != '':
                row['EVT'] = v.replace('-', '')
                row['USRID'] = int(k)

                result_csv.append(row)
        data = pd.DataFrame(result_csv).sort_values('USRID')
        data.to_csv(self.data.output.prep_evt_have_log_usr_test, index=False, sep='\t')


if __name__ == "__main__":
    runtime.start()
    usr_evt = UsrEvtTestCSV()
    usr_evt.get_evt_times()
    runtime.end()
