__author__ = 'soroush'
import numpy


class Training():
    def __init__(self, data_path, class_col, train_data):
        self.data_path = data_path              # data full path
        self.class_col = class_col              # class column
        self.train_data = train_data            # amount of train data by percent