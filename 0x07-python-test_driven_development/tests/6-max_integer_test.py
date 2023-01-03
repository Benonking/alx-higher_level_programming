#!/usr/bin/pythom3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    run test with python3 -m unittest -v tests.6-max_integer_text
    """
    def test_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_function_docstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)
    
    def test_signed_ints_and_floats(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, -4, 2, 3]), 3)
        self.assertEqual(max_integer([-1.5, -2.5]), -1.5)
        self.assertEqual(max_integer([{1, 9}, {3}, {2}, {1}]), {1, 9})

    def test_list_of_strings(self):
        self.assertEqual(max_integer("8967"), '9')
        self.assertEqual(max_integer("afvned"),'v')
        self.assertEqual(max_integer(["a", "z", "d", "e"]), "z")
        self.assertEqual(max_integer(["abc", "x"]), "x")

    def test_lists(self):
        self.assertEqual(max_integer([[1,5], [1,4]]), [1, 5])

    def test_other_sequences(self):
        with self.assertRaises(TypeError):
            max_integer({24, 1}, {1, 3})
        with self.assertRaises(TypeError):
            max_integer({1, 4, 4, 5})
        with self.assertRaises(TypeError):
            max_integer([-3, 4, 6, 'str', {1, 5}])
        with self.assertRaises(TypeError):
            max_integer([None, True])

    def test_none(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

    if __name__ == "__main__":
        unittest.main()
