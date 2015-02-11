__author__ = 'soroush'
import numpy
from core import dtree


class Testing():
    def __init__(self, d_tree, test_data, class_col):
        self.d_tree = d_tree
        self.test_data = test_data
        self.class_col = class_col
        self.tree_shape = self.test_data.shape
        self.error = 0
        self.d_tree.print_tree()

    def start_testing(self):
        for i in range(0, self.tree_shape[0]):
            row = self.test_data[i, :]
            self.test_it(row, self.d_tree)
        return self.error

    def test_it(self, row, tree):
            val = tree.attr_name
            new_tree = tree.childs.get(row[val])
            if isinstance(new_tree, type(1)):
                if row[self.class_col] != new_tree:
                    self.error += 1
            elif isinstance(new_tree, type(tree)):
                self.test_it(row, new_tree)