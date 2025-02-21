import unittest
from multiplication import my_mult

class TestMult(unittest.TestCase):

    def test_mult(self):
        """
        Test multiplication on a list
        """
        self.assertEqual(my_mult([1, 2, 3, 4]), 24, "Should be 24")

    def test_mult_tuple(self):
        """
        Test multiplication on a tuple
        """
        self.assertEqual(my_mult((1, 2, 3)), 6, "Should be 6")

    def test_float_list(self):
        """
        Check that floats are multiplied correctly
        """
        self.assertEqual(my_mult([0.5, 0.2]), 0.1, "Should be 0.1")

    def test_empty_list(self):
        """
        Multiplicative identity of an empty set is 1
        https://en.wikipedia.org/wiki/Empty_set#Operations_on_the_empty_set
        """
        self.assertEqual(my_mult([]), 1, "Should be 1")

    def test_invalid_input(self):
        my_string = "foo"
        with self.assertRaises(TypeError):
            result = my_mult(my_string)

if __name__ == '__main__':
    unittest.main()