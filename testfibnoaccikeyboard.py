import unittest

class TestFibonacciNumbersKeyboard(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(fibonacci_numbers_keyboard(""), "The following numbers are in the Fibonacci sequence:\n")
    
    def test_single_number_in_sequence(self):
        self.assertEqual(fibonacci_numbers_keyboard("13"), "The following numbers are in the Fibonacci sequence:\n13\n")
    
    def test_single_number_not_in_sequence(self):
        self.assertEqual(fibonacci_numbers_keyboard("10"), "The following numbers are in the Fibonacci sequence:\n")
    
    def test_multiple_numbers_mixed(self):
        self.assertEqual(fibonacci_numbers_keyboard("0 1 2 3 4 5 6 7 8 9"), "The following numbers are in the Fibonacci sequence:\n0\n1\n2\n3\n5\n8\n")
    
    def test_multiple_numbers_none(self):
        self.assertEqual(fibonacci_numbers_keyboard("4 6 7 10"), "The following numbers are in the Fibonacci sequence:\n")
    
if __name__ == '__main__':
    unittest.main()

