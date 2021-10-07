#!/usr/bin/python3
"""
5. Max integer - Unittest
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Since the beginning you have been creating
    “Interactive tests”. For this exercise, you will add Unittests.
    """

    def test_max_integer_list(self):
        self.assertEqual(max_integer([1, 90, 2, 13, 34, 5,
                                      -13, 3, 102, 12, 1, 5, 3]), 102)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([9, -1, 2, 3, 4, -30, 2]), 9)
        self.assertEqual(max_integer([-9, -1, -2, -3, -4, -30, -2]), -1)
        self.assertEqual(max_integer([1, 1]), 1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([10.1, 8.2, 1000.9, -10000.9]), 1000.9)
        self.assertEqual(max_integer(["1a2", "2k3"]), "2k3")
        self.assertEqual(max_integer([False, True]), True)

    def test_max_integer_non_list(self):
        self.assertEqual(max_integer("Holberton"), "t")
        self.assertEqual(max_integer("1a9"), "a")
        self.assertEqual(max_integer("1.a9"), "a")
        self.assertEqual(max_integer((1, 50, 49)), 50)
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(""), None)

    def test_max_integer_error(self):
        with self.assertRaises(TypeError):
            max_integer([4, "H"])
            max_integer(1)
            max_integer(1, 2)
            max_integer(None)
            max_integer(True)
        with self.assertRaises(KeyError):
            max_integer({"a": 1, "b": 4})


if __name__ == '__main__':
    unittest.main()
