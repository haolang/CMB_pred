from sklearn.feature_extraction.text import TfidfVectorizer
from src.common.time_used import runtime
import pandas as pd
import numpy as np
import src.common.my_data as my_data
from sklearn.linear_model import LassoCV
from sklearn.model_selection import train_test_split,StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

class TfIdf:

    def __init__(self):
        self.data = my_data.Data()   # 数据的路径类
        self.params = dict(
            min_df=0.01,  # 事件文档中的出现次数高于次值才纳入tfidf中计算
            max_df=0.90,  # 在文档中出现比例低于次值才纳入tf-idf中计算
            sublinear_tf=True,
            stop_words=None
        )

    def base_tfidf_feature(self, path):

        """
        使用tf-idf提取文档特征，也就是表示文档，基于侧袋模型
        1、演示tf-idf的用法，关键词提取
        参数信息：
        输入：list of str   str是用空格分割的好的单词 输入数据格式为： list of list[word] 或者 list of string[必须满足是空格切分的单词]
        1.1、smooth_idf: idf平滑参数，默认为True，idf=ln((文档总数+1)/(包含该词的文档数+1))+1，如果设为False，idf=ln(文档总数/包含该词的文档数)+1
        1.2、max_features：默认为None，可设为int，对所有关键词的ifidf进行降序排序，只取前max_features个作为关键词集
        1.3、min_df：包含词语的文档最小个数，如果某个词的document frequence小于min_df，则这个词不会被当作关键词，如果是float类型[0,1],则表示文档频率
        1.4、max_df：同上
        1.5、itidf用于表示文本 也就是content
        1.6、ngram_range：（1，3）表示3-1个特征进行组合，生成新的特征
        """

        # 读取一定数量:train_num的数据来训练tfidf

        documents = pd.read_table(path)['EVT']  #  .values.astype('U')
        print("documents : ", documents.shape)
        # print(documents)
        tfv = TfidfVectorizer(min_df=self.params['min_df'], max_df=self.params['max_df'],
                              sublinear_tf=self.params['sublinear_tf'], stop_words=self.params['stop_words'])
        # 此时获得的特征过于稀疏，维度太高，不能直接使用
        # 训练tfidf模型,统计了每个单词的在每篇文章中的tfidf

        # 返回的result是一个matrix，行是文本的个数，列是词语的个数

        tfv_result = tfv.fit_transform(documents).toarray()
        print("tfv_result")
        names = np.array(tfv.get_feature_names())

        tfv_pdDF = pd.DataFrame(data=tfv_result, columns=names)

                        # penalty = pd.read_csv(self.data.output.f_token_penalty)['penalty']
                        # print("penalty  ", penalty.shape)

                        # tfv_pdDF.drop(self.drop_list(tfv_pdDF, penalty, names), axis=1, inplace=True)
                        # print(tfv_pdDF.shape)
        print(tfv_pdDF)
        return tfv_pdDF

    # 返回需要删除掉的列头标label
    def drop_list(self, tfidf, y_train, names):
        lasso = LassoCV()
        lasso.fit(tfidf, y_train)
        coef = pd.Series(lasso.coef_, index=tfidf.columns)
        # print("Lasso picked " + str(sum(coef != 0)) + " variables and eliminated the other " + str(
        #     sum(coef == 0)) + " variables")
        # print("coef : ",coef)
        delete_list = []
        for i in range(len(coef)):
            if coef[i] < 0.05:
                delete_list.append(tfidf.columns[i])
        # print("delete list :", delete_list)
        return delete_list

    def save_ftidf_feature_csv(self):

        read_data = self.data.output.prep_usr_evt
        save_feature = self.data.feature.tf_idf_evt

        # read_data = self.data.output.prep_evt_have_log_usr
        # save_feature = self.data.feature.tf_idf_have_log_usr_evt

        # names, tfv_result = self.base_tfidf_feature(read_data)
        pd_dataframe = self.base_tfidf_feature(read_data)
        pd_dataframe.to_csv(save_feature, index=False, sep='\t')
        # print(data)
        # pd.DataFrame(data=tfv_result, columns=names).to_csv(save_feature, index=False,  encoding="uft-8")


if __name__ == "__main__":
    runtime.start()
    tf_idf = TfIdf()
    tf_idf.save_ftidf_feature_csv()
    # print(tf_idf.num_class())
    # tf_idf.lr_tfidf_stack()
    # tf_idf.base_tfidf_feature()
    runtime.end()
