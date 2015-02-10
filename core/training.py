__author__ = 'soroush'
import numpy
from core import dtree


class Training():
    def __init__(self, data_path, class_col, train_data, selection_type):
        self.data_path = data_path                                         # data full path
        self.class_col = class_col                                         # class column
        self.train_data_p = train_data/100                                 # amount of train data
        self.selection_mode = selection_type                               # mode of choosing training data
        self.file = open(data_path, 'r')                                   # data file stream
        self.total_rows = 625                                              # total rows of a file
        self.data_string = self.file.readline()                            # converting contents to string
        self.data_array = numpy.fromstring(self.data_string, dtype=int, sep=',').reshape((self.total_rows, 5))
        self.train_rows = int(self.total_rows * self.train_data_p)         # total rows of training data
        self.e_start_total = 0                                             # Starting Entropy for each step of splitting
        self.inf_gain = []                                                 # temporary list for holding information gain
        self.temp_array = numpy.array((0, 1))                              # just a temporary array for setting Inf gain
        if self.selection_mode == 'F':
            self.training_array = self.data_array[0:self.train_rows, 0:5]
        elif self.selection_mode == 'E':
            self.training_array = self.data_array[self.total_rows-self.train_rows-1:self.total_rows, 0:5]

    def set_class_col(self):
        if self.class_col == 'first':
            self.class_col = 0
        if self.class_col == 'last':
            self.class_col = 4

    def start_training(self):
        self.set_class_col()
        self.set_e_start(self.training_array)
        for i in range(0, 4):
            if all(self.training_array[:, i] == 0):
                continue
            else:
                self.inf_gain.append(self.set_inf_gain(self.training_array, i))
        col_to_split = self.get_max_inf_gain(self.inf_gain)  # column to split)
        cts_values = numpy.unique(self.training_array[:, col_to_split]).tolist()  # column to split values
        a = dtree.DTree(col_to_split, cts_values)
        for c in cts_values:
            temp = self.training_array[self.training_array[:, col_to_split] == c]
            temp[:, col_to_split] = 0
            self.build_tree(temp, a, c)
        return a

    def build_tree(self, temp, tree, c):
        class_values = numpy.unique(temp[:, self.class_col]).tolist()
        for i in class_values:
            if all(temp[:, self.class_col] == i):
                tree.add_leaf(c, i)
                return 'end'
        self.inf_gain = []
        self.set_e_start(temp)
        for i in range(0, 4):
            if all(temp[:, i] == 0):
                self.inf_gain.append(-200000)
            else:
                self.inf_gain.append(self.set_inf_gain(temp, i))
        col_to_split = self.get_max_inf_gain(self.inf_gain)  # column to split
        cts_values = numpy.unique(temp[:, col_to_split]).tolist()  # column to split values
        b = dtree.DTree(col_to_split, cts_values)
        tree.add_child(c, b)
        for p in cts_values:
            tmp = temp[temp[:, col_to_split] == p]
            tmp[:, col_to_split] = 0
            self.build_tree(tmp, b, p)

    '''     First step of C4.5 algorithm is calculating 'Starting Entropy' of training data.
            We call it e_start and use the following function to calculate it      '''

    def set_e_start(self, array):
        arr = numpy.unique(array[:, self.class_col]).tolist()
        for i in arr:
            [m, n] = array[array[:, self.class_col] == i].shape
            self.e_start_total -= (m/self.train_rows)*numpy.log2(m/self.train_rows)

    '''     After that we should calculate the 'New Entropy' for each column and then
            difference between Starting Entropy and New Entropy gives us 'Information Gain'
            of each column.                                                              '''

    def set_inf_gain(self, array, col_number):
        self.temp_array = array
        arr = numpy.unique(self.temp_array[:, col_number]).tolist()
        col_e_new = 0
        this_total_rows = 0
        for i in arr:
            x = self.temp_array[self.temp_array[:, col_number] == i]
            [m, n] = x.shape
            this_total_rows += m
            arr2 = numpy.unique(x[:, self.class_col]).tolist()
            for j in arr2:
                [o, p] = x[x[:, self.class_col] == j].shape
                col_e_new -= (o*numpy.log2(o))
            col_e_new += (m*numpy.log2(m))
        col_e_new = col_e_new / this_total_rows
        return self.e_start_total - col_e_new

    def get_max_inf_gain(self, inf_gain):
        max_index = -1
        ma_x = -1
        for i in range(len(inf_gain)):
            if inf_gain[i] > ma_x:
                ma_x = inf_gain[i]
                max_index = i
        return max_index