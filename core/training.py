__author__ = 'soroush'
import numpy


class Training():
    def __init__(self, data_path, class_col, train_data, selection_type):
        self.data_path = data_path                                                      # data full path
        self.class_col = class_col                                                      # class column
        self.train_data_p = train_data/100                                              # amount of train data
        self.selection_mode = selection_type                                            # mode of choosing training data
        self.file = open(data_path, 'r')                                                # data file stream
        self.total_rows = 625                                                           # total rows of a file
        self.data_string = self.file.readline()                                         # converting contents to string
        self.data_array = numpy.fromstring(self.data_string, dtype=int, sep=',').reshape((self.total_rows, 5))
        self.train_rows = int(self.total_rows * self.train_data_p)                      # total rows of training data
        self.e_start_total = 0
        if self.selection_mode == 'F':
            self.training_array = self.data_array[0:self.train_rows, 0:5]
        elif self.selection_mode == 'E':
            self.training_array = self.data_array[self.total_rows-self.train_rows-1:self.total_rows, 0:5]

    def start_training(self):
        if self.class_col == 'first':
            self.class_col = 4
        if self.class_col == 'last':
            self.class_col = 0
        self.set_e_start_total()

    '''     First step of C4.5 algorithm is calculating 'Starting Entropy' of training data.
            We call it e_start_total and use the following function to calculate it      '''

    def set_e_start_total(self):
        arr = numpy.unique(self.training_array[:, self.class_col]).tolist()
        for i in arr:
            [m, n] = self.training_array[self.training_array[:, self.class_col] == i].shape
            self.e_start_total -= (m/self.train_rows)*numpy.log2(m/self.train_rows)

    def inf_gain(self):
        pass