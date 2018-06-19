from src.common.my_data import Data
from src.common.time_used import runtime
import pandas as pd


class NoLogUsrTest:

    def __init__(self):
        self.data = Data()

    def get_evt_times(self):

        evt_datas = pd.read_table(self.data.output.sorted_test_log)
        usr_ids = set(pd.read_table(self.data.output.sorted_test_agg)['USRID'])
        print("usr_id ： ", usr_ids)
        result = dict()

        for usr_id in usr_ids:
            usr_id = str(usr_id)
            result[usr_id] = ''

        for usr_id_log in evt_datas['USRID']:
            usr_id_log = str(usr_id_log)
            if result[usr_id_log] == '':
                result[usr_id_log] = '1'
            # else:
                # result[usr_id_log] += " " + evt_log

        result_csv = []

        for k, v in result.items():  # k > id
            # k = str(k)
            # result_csv['USRID'] = k
            row = dict()
            if v == '':
                # v = '0'
                # row['EVT'] = v.replace('-', '')
                row['USRID'] = k
                result_csv.append(row)
        print(result)
        data = pd.DataFrame(result_csv)
        data.to_csv(self.data.output.no_log_usr_test, index=False, sep='\t')


if __name__ == "__main__":
    runtime.start()
    usr_evt = NoLogUsrTest()
    usr_evt.get_evt_times()
    runtime.end()
