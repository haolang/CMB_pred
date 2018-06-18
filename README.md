# CMB_pred

> ### 开发流程
数据预处理：
	
1. 数据处理：
    * 数据源：train_agg.csv
    * 处理方法：依据train_agg.csv 中的USRID值对行升序排序，使之数据与train_flg.csv中的USRID顺序一一对应
    * 数据源：train_flg.csv，train_log.csv
    * 处理方法：同上
2. 数据提取：
    * 数据源：train_log
    * 处理方法：统计同一 EVT_LBL 模块打开的频次，同一EVT_LBL 模块的平均打开间隔时间,同一模块打开次数,没有打开模块记录则，EVT_FRQ ，AVG_O_TIME ，EVT_TIMES均设为0
    * 数据列名（共4列）：USRID  |  EVT_FRQ  |  AVG_O_TIME  |  EVT_TIMES


### 参考链接

> [无监督︱异常、离群点检测 一分类——OneClassSVM](https://blog.csdn.net/sinat_26917383/article/details/76647272)