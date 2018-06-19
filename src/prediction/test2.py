import pandas as pd
from sklearn.model_selection import train_test_split
from src.common.my_data import Data
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import hamming_loss


class Test2EvtTiems:
    def __init__(self):
        self.data = Data()

    def pre(self):
        # usr_id = pd.read_table(self.data.output.sorted_train_agg)["USRID"]

        x2 = pd.read_table(self.data.output.prep_evt_times).drop(labels="USRID", axis=1)
        print(x2.shape)
        y2 = pd.read_table(self.data.output.sorted_train_flg)['FLAG']
        print(y2.shape)
        train_x2, test_x2, train_y2, test_y2 = train_test_split(x2, y2, test_size=0.2)

        model2 = LogisticRegression()
        model2.fit(train_x2, train_y2)
        pred_y2 = model2.predict(test_x2)
        print(pred_y2)
        test_y2 = list(test_y2)
        count2 = 0
        test_y_count2 = 0
        for x2, y2 in zip(pred_y2, test_y2):
            if y2 == 1:
                test_y_count2 += 1

            if x2 == y2 and x2 == 1:
                count2 += 1
        if test_y_count2 == 0:
            test_y_count2 = 1
        print("test2 准确率： ", count2 / test_y_count2)
        print("test2 损失率 ", hamming_loss(test_y2, pred_y2))
        return pred_y2, test_y2


if __name__ == "__main__":
    test = Test2EvtTiems()
    test.pre()
