
import pandas as pd
import numpy as np
from src.common.my_data import Data
from sklearn.linear_model import LassoCV
from sklearn.linear_model import MultiTaskLasso

data = Data()

agg_train_have_log = pd.read_table(data.output.sorted_train_agg_have_log_usr).drop('USRID', axis=1)
print('agg_train_have_log : ', agg_train_have_log.shape)
agg_test_have_log = pd.read_table(data.output.sorted_test_agg_have_log_usr).drop('USRID', axis=1)
print('agg_test_have_log : ', agg_test_have_log.shape)
agg_all_have_log = pd.concat([agg_train_have_log, agg_test_have_log], axis=0)
print('agg_all_have_log : ', agg_all_have_log.shape)

tf_idf_all_have_log = pd.read_table(data.feature.tf_idf_have_log_usr_evt_all)
tf_idf_all_have_log_name = tf_idf_all_have_log.head(0)
print(tf_idf_all_have_log_name)
print('tf_idf_all_have_log : ', tf_idf_all_have_log.shape)
# print(tf_idf_all)

agg_no_have_log = pd.read_table(data.output.sorted_test_agg_no_have_log_usr).drop('USRID', axis=1)

print('agg_no_have_log : ', agg_no_have_log.shape)

lasso = MultiTaskLasso()
lasso.fit(agg_all_have_log, tf_idf_all_have_log)
result_lasso = lasso.predict(agg_no_have_log)
print(result_lasso)
# result_csv = pd.DataFrame(result_lasso)
# data.to_csv(data.output.prediction_test_no_log_tf_idf, index=False, sep='\t')
