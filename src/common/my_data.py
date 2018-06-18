
class DataInput:

    def __init__(self, root_path):
        self.train_data_path = root_path + r'\input\train.txt'
        self.stop_data_path = root_path + r'\input\stop.txt'
        self.test_data_path = root_path + r'\input\test.txt'
        self.law_data_path = root_path + r'\input\law.txt'


class DataOutput:
    def __init__(self, root_path):
        # 初始化训练数据
        self.f_token_all = root_path + r'\output\f_token_all.csv'
        self.f_token_content = root_path + r'\output\f_token_content.csv'
        self.f_token_penalty = root_path + r'\output\f_token_penalty.csv'
        self.f_token_laws = root_path + r'\output\f_token_laws.csv'
        # 初始化测试数据
        self.f_token_test = root_path + r'\output\f_token_test.csv'


class Model:
    def __init__(self, root_path):
        self.f_w2v_model = root_path + r'\model\f_w2v_model'


class Feature:
    def __init__(self, root_path):
        # w2v feature
        self.f_w2v_feature_train = root_path + r'\feature\f_w2v_feature_train.csv'
        self.f_w2v_feature_test = root_path + r'\feature\f_w2v_feature_test.csv'
        # tf-idf
        self.f_tf_idf_feature = root_path + r'\feature\f_tf_idf_feature.csv'
        self.f_tf_idf_feature_test = root_path + r'\feature\f_tf_idf_feature_test.csv'
        # lda feature
        self.f_lda_feature = root_path + r'\feature\f_lda_feature.csv'
        self.f_lda_feature_test = root_path + r'\feature\f_lda_feature_test.csv'


class Data:
    def __init__(self):
        self.root_path = r'D:\study\big_data\mycode\law_case\data'
        self.input = DataInput(self.root_path)
        self.output = DataOutput(self.root_path)
        self.model = Model(self.root_path)
        self.feature = Feature(self.root_path)
