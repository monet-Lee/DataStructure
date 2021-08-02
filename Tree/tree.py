
"""
File: buildtree
Author: YaoLee
"""

class MyNode(object):
    """Represents a singly linked node"""

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


class tree(MyNode):
    #构建一个搜索二叉树

    def __init__(self):
        self.root = None

    def add(self, item):

        def recurse(node):

            if item <node.data:
                if node.left ==None:
                    node.left = MyNode(item)
                else:
                    recurse(node.left)
            elif node.right == None:
                node.right=MyNode(item)
            else:
                recurse(node.right)
        if self.root == None:
            self.root=MyNode(item)
        else:
            recurse(self.root)

if __name__ == '__main__':
    mytree = tree()
    mytree.add('A')
    mytree.add('K')
    mytree.add('D')
    mytree.add('A')

    print(mytree)

