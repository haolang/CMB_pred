
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
        self.sorted_train_flg = root_path + r'\output\sorted_train_flg.csv'
        self.sorted_train_log = root_path + r'\output\sorted_train_log.csv'


class Model:
    def __init__(self, root_path):
        pass
        # self. = root_path + r'\model\'


class Feature:
    def __init__(self, root_path):
        pass
        # self.*** = root_path + r'\feature\***.csv'

class Data:
    def __init__(self):
        self.root_path = r'D:\study\big_data\mycode\CMB_pred\data'
        self.input = Input(self.root_path)
        self.output = Output(self.root_path)
        self.model = Model(self.root_path)
        self.feature = Feature(self.root_path)
