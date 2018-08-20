import unittest

'''
Description: A dictionary class designed with arrays within an array that utilizes chaining as a way to handle collisions. 
Author: Satinder Jamal

'''

'''
    Implement a dictionary using chaining.
    You may assume every key has a hash() method, e.g.:
    >>> hash(1)
    1
    >>> hash('hello world')
    -2324238377118044897
'''


class dictionary:
    def __init__(self, init=None):
        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)] #dictionary
        self.__count = 0

        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        return self.__count

    def flattened(self):
        return [item for inner in self.__items for item in inner]

    def __iter__(self):
        return (iter(self.flattened()))

    def checkload(self):
        return self.__count/self.__limit

    def __str__(self):
        return (str(self.flattened()))

    def findIndex(self, key):
        return hash(key) % self.__limit

    def __setitem__(self, key, value):
        index = self.findIndex(key)
        if not self.__contains__(key):
            self.__items[index].append([key, value])
            self.__count += 1
        if self.__count >= self.__limit * .75:
            self.loaded()

    def loaded(self):
        oldHash = self.__iter__()
        self.__limit = self.__limit * 2
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0
        for x in oldHash:
            self.__setitem__(x[0], x[1])

    def underload(self):
        oldHash = self.flattened()
        self.__limit = self.__limit // 2
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0
        for x in oldHash:
            self.__setitem__(x[0], x[1])

    def __getitem__(self, key):
        index = self.findIndex(key)
        for slot in self.__items[index]:
            if slot[0] == key:
                return slot[1]

    def __contains__(self, key):
        list1 = self.flattened()
        for i in list1:
            if i[0] == key:
                return True
        return False

    def __delitem__(self, key):
        index = hash(key) % self.__limit
        if index < 0 or index > self.__limit:
            raise Exception("Item Not Found")
        for i in range(len(self.__items[index])):
            item = self.__items[index][i]
            if item[0] == key:
                del self.__items[index][i]
                self.__count -= 1
        if self.__count <= self.__limit * .25:
            self.underload()
        return

    def keys(self):
        flatlist = self.flattened()
        keylist = []
        if len(flatlist) == 0:
            return None
        for x in flatlist:
            keylist.append(x[0])
        return keylist

    def values(self):
        flatlist = self.flattened()
        keylist = []
        if len(flatlist) == 0:
            return None
        for x,i in flatlist:
            keylist.append(i[0:])
        return keylist






''' C-level work '''


class test_add_two(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")

class test_add_twice(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[1] = "one"
        self.assertEqual(len(s), 1)
        self.assertEqual(s[1], "one")

class test_store_false(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = False
        self.assertTrue(1 in s)
        self.assertFalse(s[1])


class test_store_none(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = None
        self.assertTrue(1 in s)
        self.assertEqual(s[1], None)

class test_none_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[None] = 1
        self.assertTrue(None in s)
        self.assertEqual(s[None], 1)

class test_False_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[False] = 1
        self.assertTrue(False in s)
        self.assertEqual(s[False], 1)

class test_collide(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[10] = "ten"
        self.assertEqual(len(s), 2)
        self.assertTrue(0 in s)
        self.assertTrue(10 in s)
        self.assertEqual(s[10],"ten")
        self.assertEqual(s[0],"zero")


class test_delitem__(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] =  "five"
        s.__delitem__(5)
        self.assertEqual(len(s), 4)

class test_loaded(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        s[6] = "six"
        s[7] = "seven"
        self.assertEqual(len(s), 7)
        s[8] = "eight"
        self.assertEqual(s.checkload(), 0.4)

class test_underload(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s.__delitem__(3)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.checkload(), 0.4)

class test_keys(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        self.assertEqual(s.keys(), [1])
        s[2] = "two"
        s[3] = "three"
        self.assertEqual(s.keys(), [1, 2, 3])

class test_values(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        self.assertEqual(s.values(), ["one", "two", "three"])
'''
B-level work
    Add doubling and rehashing when load goes over 75%
    def newFuntion():
    Add __delitem__(self, key)
    def test_delitem(self, key)
        s
'''

''' A-level work
    Add halving and rehashing when load goes below 25%
    Add keys() add python keys and dictionary return a list of keys for dictionary
    Add values() return a list of values for dictionary and write test for all. 
'''

''' Extra credit
    Add __eq__()
    Add items(), "a list of D's (key, value) pairs, as 2-tuples"
'''

if __name__ == '__main__':
    unittest.main()
