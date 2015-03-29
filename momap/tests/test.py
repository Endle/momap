import unittest
import sys
sys.path.append("../")
import momap

class Test_momap(unittest.TestCase):
    def test_init(self):
        m = momap.momap()
        self.assertEqual(repr(m), "momap{}")
        m = momap.momap(a=1, b=2)
        self.assertEqual(repr(m), "momap{a: [1], b: [2]}")
        m = momap.momap([('a', 1), ('b', 2), ('c', 4), ('a', 2)])
        self.assertEqual(repr(m), "momap{a: [1, 2], b: [2], c: [4]}")

    def test_getset(self):
        m = momap.momap()
        m['a'] = 5
        self.assertEqual(m['a'], 5)
        m.add('a', 7)
        self.assertEqual(m['a'], 5)
        m['a'] = 5
        m.add('a', 7)
        self.assertEqual(repr(m), "momap{a: [5, 7]}")

    def test_contains(self):
        m = momap.momap([('a', 1), ('b', 2), ('c', 4), ('a', 2)])
        self.assertTrue('a' in m)
        self.assertFalse('e' in m)

    def test_get_list(self):
        m = momap.momap([('a', 1), ('b', 2), ('c', 4), ('a', 2)])
        self.assertEqual(m.get_list('a'), [1, 2])

    def test_iter(self):
        m = momap.momap([('a', 1), ('b', 2), ('c', 4), ('a', 2)])
        it = iter(m)
        self.assertEqual(list(it), ['a', 'b', 'c'])

    def test_len(self):
        m = momap.momap()
        self.assertEqual(len(m), 0)
        m = momap.momap([('a', 1), ('b', 2), ('c', 4), ('a', 2)])
        self.assertEqual(len(m), 3)

    def test_items(self):
        m = momap.momap([('a', 1), ('b', 2), ('c', 4), ('a', 2)])
        li = list(m.items())
        self.assertEqual(li, [('a', [1, 2]), ('b', [2]), ('c', [4])])

    def test_extend(self):
        m = momap.momap([('a', 1), ('b', 2)])
        m.extend('a', [2, 5, "tree"])
        self.assertEqual(repr(m), "momap{a: [1, 2, 5, 'tree'], b: [2]}")

if __name__ == '__main__':
    unittest.main()

