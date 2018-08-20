import unittest
from queue import *

class binary_search_tree:
    def __init__ (self, init: object = None) -> object:
        self.__value = self.__left = self.__right = None

        if init:
            for i in init:
                self.add(i)


    def __iter__(self):
        if self.__left:
            for node in self.__left:
                yield(node)

        yield(self.__value)

        if self.__right:
            for node in self.__right:
                yield(node)

    def __str__(self): 
        return(','.join(str(node) for node in self))


    def add(self, value):
        if self.__value is None:
            self.__value = value
        else:
            if value < self.__value:
                if self.__left is None:
                    self.__left = binary_search_tree([value])
                else:
                    self.__left.add(value)

            if value > self.__value:
                if self.__right is None:
                    self.__right = binary_search_tree([value])
                else:
                    self.__right.add(value)



    def preorder(self):
        consecvals = []
        if self.__value is None:
            return [self.__value]
        else:
            consecvals += [self.__value]

        if self.__left:
            consecvals += self.__left.preorder()

        if self.__right:
            consecvals += self.__right.preorder()

        return consecvals

    def inorder(self):
        consecvals = []
        if self.__value is None:
            return [self.__value]

        if self.__left:
            consecvals += self.__left.inorder()
        consecvals += [self.__value]

        if self.__right:
            consecvals += self.__right.inorder()

        return consecvals



    def postorder(self):
        consecvals = []
        if self.__value is None:
            return [self.__value]

        if self.__left:
            consecvals += self.__left.postorder()
        if self.__right:
            consecvals += self.__right.postorder()

        consecvals += [self.__value]
        return consecvals

    def BFS(self):
        queue = [self]
        result = []

        while queue:
            temp = queue.pop(0)
            result.append(temp.__value)

            if temp.__left:
                queue.append(temp.__left)
            if temp.__right:
                queue.append(temp.__right)

        return result



class test_binary_search_tree (unittest.TestCase):
    '''
           20q
          /  \
        10   30
            /  \
           25  35
    '''

    # C level
    def test_empty(self):
        self.assertEqual(str(binary_search_tree()), 'None')
    def test_one(self):
        self.assertEqual(str(binary_search_tree([1])), '1')
    def test_add(self):
        bt = binary_search_tree()
        bt.add(20)
        bt.add(10)
        bt.add(30)
        bt.add(25)
        bt.add(35)
        self.assertEqual(str(bt), '10,20,25,30,35')
    def test_init(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(str(bt), '10,20,25,30,35')


    # B level

    def test_empty_inorder(self):
        self.assertEqual(binary_search_tree().inorder(), [None])

    def test_inorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.inorder(), [10, 20, 25, 30, 35])

    def test_preorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(list(bt.preorder()), [20, 10, 30, 25, 35])

    def test_postorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.postorder(), [10, 25, 35, 30, 20])


    # A level

    def test_empty_BFS(self):
        self.assertEqual(binary_search_tree().BFS(), [None])

    def test_BFS(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.BFS(), [20, 10, 30, 25, 35])


if '__main__' == __name__:
    unittest.main()
