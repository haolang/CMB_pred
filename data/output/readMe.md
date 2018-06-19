# 文件说明
>###文件结构
```
├─feature
│      tf_idf_evt.csv
│      tf_idf_have_log_usr_evt.csv
│      
├─input
│      test_agg.csv
│      test_log.csv
│      train_agg.csv
│      train_flg.csv
│      train_log.csv
│      
├─model
└─output
        no_log_usr.csv
        prediction_flg.csv
        prep_evt_have_log_usr.csv
        prep_evt_interval.csv
        prep_evt_times.csv
        prep_usr_evt.csv
        readMe.md
        sorted_train_agg.csv
        sorted_train_agg_have_log_usr.csv
        sorted_train_flg.csv
        sorted_train_flg_have_log_usr.csv
        sorted_train_log.csv
        train_agg_flg_0.csv
        train_agg_flg_1.csv
        文件说明.url
```

**数据读取建议用 pd.read_table(),csv数据分割符均使用 \t**
### prediction_flg.csv
> 预测结果表格
- 表格格式如下：

USRID  | FLAG 
:----: | :----:  
用户ID | 预测结果值 

***

### prep_evt_interval.csv
> 用户点击对应事件的最大时间差

0-221-267 | 0-222-268 | ... | 604-2167-4398 | USRID
:----: | :----: | :---: | :---:|:---:
最大时间间隔 | 最大时间间隔 | ... | 最大时间间隔| 用户ID

*最大时间间隔为0则用户未查看该事件*

***

### prep_evt_interval.csv
> 用户点击对应事件的最大时间差

0-221-267 | 0-222-268 | ... | 604-2167-4398 | USRID
:----: | :----: | :---: | :----: | :---:
点击次数 | 点击次数 | ... | 点击次数 | 用户ID
***
### prep_usr_evt.csv
> 用户点击过的事件

EVT | USRID 
:----: | :----: 
事件 | 用户ID 

*多个事件用 空格‘ ’分割，无事件则数值为0*
***
### prep_evt_have_log_usr.csv
> 有log记录的用户点击过的事件

EVT | USRID 
:----: | :----: 
事件 | 用户ID 

*多个事件用 空格‘ ’分割，无事件则数值为0*

***
### no_log_usr.csv
> 没有log数据的用户对应的用户ID

USRID | 
:----: |
用户ID |

***
### tf_idf_evt.csv
> 根据 prep_usr_evt.csv 文件得到的TF-IDF

163578914(EVT_ID) | ...
:----: | :---:
TF-IDF值 | ...

***

### tf_idf_have_log_usr_evt.csv
> 根据 prep_evt_have_log_usr.csv 文件得到的TF-IDF

101515(EVT_ID) | ...
:----: | :---:
TF-IDF值 | ...

***
### sorted_train_agg_have_log_usr.csv
> 根据 sorted_train_agg.csv 和no_log_usr.csv 筛选得到,在log文件中存在相应的USRID则在此文件中有对应的agg

V1 | V2 | ... | V30 | USRID
:----: | :---: | :---: | :---: | :---: 
v1 | v2 | ... | v30 | 用户ID | 

***
### sorted_train_flg_have_log_usr.csv
> 根据 sorted_train_flg.csv 和no_log_usr.csv 筛选得到,在log文件中存在相应的USRID则在此文件中有对应的agg

USRID | FLAG
:----: | :---: 
用户ID | 0或1

***