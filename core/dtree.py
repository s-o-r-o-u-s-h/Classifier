__author__ = 'soroush'


class DTree():
    def __init__(self, attribute, values):
        self.attr_name = attribute  # name/value of attribute
        self.values = values  # list of attribute values
        self.childs = dict.fromkeys(self.values)  # children of a DTree node

    '''     Following function is necessary for adding a subtree to the current tree
            during the process of creating decision tree.                       '''

    def add_child(self, value, child):
        if value in self.values and self.childs[value] is None:
            self.childs[value] = DTree(child.attr_name, child.values)
        else:
            print('not allowed')

    '''     When a tree doesn't have any subtrees,it should have leave(s), Following
            function helps you to add a leaf to the current tree.               '''

    def add_leaf(self, value, leaf):
        if value in self.values and self.childs[value] is None:
            self.childs[value] = leaf

    '''     Sometimes you need a basic printing function to see your tree, This
            function helps to search a tree without any specific approach we
            know in Graph search algorithms.                                    '''

    def print_tree(self):
        print('att', self.attr_name, 'values:')
        for i in self.values:
            print(i)
            if isinstance(self.childs[i], type(1)):
                print('class:', self.childs[i])
            elif isinstance(self.childs[i], DTree):
                DTree.print_tree(self.childs[i])
            else:
                print('None found')
        print('EOT')