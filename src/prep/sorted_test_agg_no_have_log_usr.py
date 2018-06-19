
import pandas as pd

from src.common.my_data import Data


class TestNoUsrLogAgg:
    def __init__(self):
        self.data = Data()

    def get_usr_log_agg(self):
        sorted_train_agg = pd.read_table(self.data.output.sorted_test_agg)

        # sorted_train_agg_no_usrid = sorted_train_agg.drop('USRID', axis=1)
        # print(sorted_train_agg_no_usrid['V1'][1])
        no_log_usr = set(pd.read_table(self.data.output.no_log_usr_test)['USRID'])
        # print(no_log_usr)
        # result = []
        drop_array = []
        # print(sorted_train_agg)
        for agg_id, i in zip(sorted_train_agg['USRID'], range(0, sorted_train_agg.shape[0])):
            # print(agg_id)
            if agg_id not in no_log_usr:
                drop_array.append(i)

        print(drop_array)
        sorted_train_agg.drop(sorted_train_agg.index[drop_array], inplace=True)
        # print('--------------------------------------------------')
        # print(sorted_train_agg)
        sorted_train_agg.to_csv(self.data.output.sorted_test_agg_no_have_log_usr, index=None, sep='\t')


if __name__ == "__main__":
    usrlogagg = TestNoUsrLogAgg()
    usrlogagg.get_usr_log_agg()
