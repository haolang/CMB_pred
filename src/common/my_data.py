import time


class Input:

    def __init__(self, root_path):
        self.test_agg = root_path + r'\input\test_agg.csv'
        self.test_log = root_path + r'\input\test_log.csv'
        self.train_agg = root_path + r'\input\train_agg.csv'
        self.train_flg = root_path + r'\input\train_flg.csv'
        self.train_log = root_path + r'\input\train_log.csv'


class Output:
    def __init__(self, root_path):
        # 排序后的用户数据
        self.sorted_train_agg = root_path + r'\output\sorted_train_agg.csv'
        self.sorted_train_agg_have_log_usr = root_path + r'\output\sorted_train_agg_have_log_usr.csv'
        self.sorted_test_agg_have_log_usr = root_path + r'\output\sorted_test_agg_have_log_usr.csv'
        self.sorted_test_agg_no_have_log_usr = root_path + r'\output\sorted_test_agg_no_have_log_usr.csv'
        self.sorted_train_flg = root_path + r'\output\sorted_train_flg.csv'
        self.sorted_train_flg_have_log_usr = root_path + r'\output\sorted_train_flg_have_log_usr.csv'
        self.sorted_train_log = root_path + r'\output\sorted_train_log.csv'
        self.sorted_test_agg = root_path + r'\output\sorted_test_agg.csv'
        self.sorted_test_log = root_path + r'\output\sorted_test_log.csv'

        # 处理后的数据
        self.prep_evt_times = root_path + r'\output\prep_evt_times.csv'
        self.prep_evt_times_have_log_usr = root_path + r'\output\prep_evt_times_have_log_usr.csv'
        self.prep_evt_interval = root_path + r'\output\prep_evt_interval.csv'
        self.prep_evt_interval_have_log_usr = root_path + r'\output\prep_evt_interval_have_log_usr.csv'
        self.prep_usr_evt = root_path + r'\output\prep_usr_evt.csv'
        self.prep_evt_have_log_usr = root_path + r'\output\prep_evt_have_log_usr.csv'
        self.prep_evt_have_log_usr_test = root_path + r'\output\prep_evt_have_log_usr_test.csv'
        self.prep_evt_test = root_path + r'\output\prep_evt_test.csv'
        self.train_agg_flg_0 = root_path + r'\output\train_agg_flg_0.csv'
        self.train_agg_flg_1 = root_path + r'\output\train_agg_flg_1.csv'
        self.no_log_usr = root_path + r'\output\no_log_usr.csv'
        self.no_log_usr_test = root_path + r'\output\no_log_usr_test.csv'

        # result
        self.prediction_flg = root_path + r'\output\prediction_flg.csv'
        self.prediction_test_no_log_tf_idf = root_path + r'\output\prediction_test_no_log_tf_idf.csv'


class Model:
    def __init__(self, root_path):
        pass
        # self. = root_path + r'\model\'


class Feature:
    def __init__(self, root_path):

        self.tf_idf_evt = root_path + r'\feature\tf_idf_evt.csv'
        self.tf_idf_have_log_usr_evt = root_path + r'\feature\tf_idf_have_log_usr_evt.csv'
        self.tf_idf_have_log_usr_evt_all = root_path + r'\feature\tf_idf_have_log_usr_evt_all.csv'
        # self.*** = root_path + r'\feature\***.csv'

class Data:
    def __init__(self):
        self.root_path = r'D:\study\big_data\mycode\CMB_pred\data'
        self.input = Input(self.root_path)
        self.output = Output(self.root_path)
        self.model = Model(self.root_path)
        self.feature = Feature(self.root_path)
