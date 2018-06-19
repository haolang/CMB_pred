import pandas as pd
from sklearn.model_selection import train_test_split
from src.common.my_data import Data
from src.common.time_used import runtime
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import hamming_loss
from sklearn.metrics import roc_auc_score


class TestEvtTiems:
    def __init__(self):
        self.data = Data()

    def pre(self):
        # usr_id = pd.read_table(self.data.output.sorted_train_agg)["USRID"]
        result = dict()
        x = pd.read_table(self.data.feature.evt_tf_idf) #.drop(labels='USRID', axis=1)
        y = pd.read_table(self.data.output.sorted_train_flg)['FLAG']
        print(x.shape)
        print(y.shape)
        train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)

        model = LogisticRegression()
        model.fit(train_x, train_y)
        pred_y = model.predict(test_x)
        print(pred_y)
        test_y = list(test_y)
        count = 0
        test_y_count = 0
        for x, y in zip(pred_y, test_y):
            if y == 1:
                test_y_count += 1

            if x == y and x == 1:
                count += 1
        if test_y_count == 0:
            test_y_count = 1
        print("test 准确率： ", count / test_y_count)
        print("test 损失率 ", hamming_loss(test_y, pred_y))
        auc = roc_auc_score(test_y, pred_y)
        print('AUC:', auc)
        # save_data_cvs_columns = ['USRID', 'RST']
        # self.save_data_cvs(result, self.data.output.prep_flg, save_data_cvs_columns)
        return pred_y, test_y


if __name__ == "__main__":
    runtime.start()
    test = TestEvtTiems()
    test.pre()
    runtime.end()
