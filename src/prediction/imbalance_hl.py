import pandas as pd
import numpy as np
from collections import Counter
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from imblearn.ensemble import BalanceCascade
from sklearn.svm import LinearSVC
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegressionCV
from sklearn.linear_model import LassoCV

from src.common.my_data import Data

result = dict()
data = Data()

X1 = pd.read_table(data.output.sorted_train_agg_have_log_usr).drop('USRID', axis=1, inplace=True)
X2 = pd.read_table(data.feature.tf_idf_have_log_usr_evt)
Y = pd.read_table(data.output.sorted_train_flg_have_log_usr)['FLAG']
X = pd.concat([X1, X2], axis=1)

# x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2)
# print('Original dataset shape {}'.format(Counter(y_train)))
test_agg = pd.read_table(data.input.test_agg)
result["USRID"] = test_agg['USRID']
test_noID = test_agg.drop('USRID', axis=1)


bc = BalanceCascade(random_state=40, estimator='adaboost')
x_res, y_res = bc.fit_sample(X, Y)
print('Resampled dataset shape {}'.format(Counter(y_res[0])))

#支持向量机
# svc = LinearSVC(dual=False)
# svc.fit(x_train,y_train)
# result_svc = svc.predict(x_test)
#
# #逻辑回归
# lgc = LogisticRegressionCV()
# lgc.fit(x_train,y_train)
# result_lgc = lgc.predict(x_test)

#线性回归
lasso = LassoCV()
lasso.fit(x_res[0], y_res[0])
result_lasso = lasso.predict(test_noID)

result['RST'] = result_lasso
save_data_cvs_columns = ['USRID', 'RST']
data_df = pd.DataFrame(result)
data_df.to_csv(data.output.prediction_flg, index=False, columns=save_data_cvs_columns, sep='\t')

# score1 = roc_auc_score(y_test, result_svc)
# score2 = roc_auc_score(y_test, result_lgc)
# score3 = roc_auc_score(y_test, result_lasso)

# print(score1)
# print(score2)
# print(score3)
