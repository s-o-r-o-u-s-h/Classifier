__author__ = 'soroush'


class DTree():
    def __init__(self, attribute, values):
        self.attr_name = attribute  # name/value of attribute
        self.values = values  # list of attribute values
        self.childs = dict.fromkeys(self.values)  # children of a DTree node

    def add_child(self, value, child):
        if value in self.values and self.childs[value] is None:
            self.childs[value] = DTree(child.attr_name, child.values)
        else:
            print('not allowed')

    def add_leaf(self, value, leaf):
        if value in self.values and self.childs[value] is None:
            self.childs[value] = leaf

    def print_tree(self):
        print('att', self.attr_name, 'vals:')
        for i in self.values:
            print(i)
            if isinstance(self.childs[i], type(1)):
                print('class:', self.childs[i])
            elif isinstance(self.childs[i], DTree):
                DTree.print_tree(self.childs[i])
            else:
                print('None')
        print('end of class')