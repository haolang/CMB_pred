import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import OneClassSVM

from src.common.my_data import Data

data = Data()
train_agg_flg_0 = data.output.train_agg_flg_0
train_agg_flg_1 = data.output.train_agg_flg_1

train = pd.read_table(train_agg_flg_0).drop('USRID', axis=1)

test = pd.read_table(train_agg_flg_1).drop('USRID', axis=1)
train_noID = train[0:70000]
test_noID = train[70000:72000].append(test[0:100])

svm = OneClassSVM()
svm.fit(train_noID)

result = svm.predict(test_noID)

result0 = result[0:2000]
result1 = result[2000:]

n_result0_0 = 0
n_result1_1 = 0
n = 0
for i in result0:
    if i == 1:
        n_result0_0+=1
        n+=1

for i in result1:
    if i == -1:
        n_result1_1+=1
        n+=1

print(n_result0_0/2000)
print(n_result1_1/100)
print(n/2100)



