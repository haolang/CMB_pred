import pandas as pd
from sklearn.model_selection import train_test_split
from src.common.my_data import Data
from sklearn.svm import OneClassSVM
from sklearn.metrics import roc_auc_score

data = Data()
result = dict()
train = pd.read_table(data.output.train_agg_flg_0).drop('USRID', axis=1)
# test = pd.read_csv(data.output.train_agg_flg_1, sep='\t').drop('USRID', axis=1)
# train_noID = train[0:70000]
# test_noID = train[70000:72000].append(test[0:100])
test_agg = pd.read_table(data.input.test_agg)
result["USRID"] = test_agg['USRID']
test_noID = test_agg.drop('USRID', axis=1)
svm = OneClassSVM()
svm.fit(train)

result_svm = svm.predict(test_noID)


for re, i in zip(result_svm, range(0, len(result_svm))):
    if re == 1:
        result_svm[i] = 0
    elif re == -1:
        result_svm[i] = 1

result['RST'] = result_svm
save_data_cvs_columns = ['USRID', 'RST']

data_df = pd.DataFrame(result)
data_df.to_csv(data.output.prediction_flg, index=False, columns=save_data_cvs_columns, sep='\t')
print(result_svm)
# auc = roc_auc_score(label, result_svm)
# print( 'AUC:',auc)
# result0 = result[0:2000]
# result1 = result[2000:]

# n_result0_0 = 0
# n_result1_1 = 0
# n = 0
# for i in result0:
#     if i == 1:
#         n_result0_0+=1
#         n+=1
#
# for i in result1:
#     if i == -1:
#         n_result1_1+=1
#         n+=1
#
# print(n_result0_0/2000)
# print(n_result1_1/100)
# print(n/2100)



