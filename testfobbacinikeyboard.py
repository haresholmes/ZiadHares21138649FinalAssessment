import unittest

class TestIsFibonacciKeyboard(unittest.TestCase):
    
    def test_fibonacci_number(self):
        self.assertEqual(is_fibonacci_keyboard(5), "5 is in the Fibonacci sequence.")
    
    def test_non_fibonacci_number(self):
        self.assertEqual(is_fibonacci_keyboard(6), "6 is not in the Fibonacci sequence.")
    
    def test_negative_number(self):
        self.assertEqual(is_fibonacci_keyboard(-1), "-1 is not in the Fibonacci sequence.")
    
    def test_zero(self):
        self.assertEqual(is_fibonacci_keyboard(0), "0 is in the Fibonacci sequence.")
    
    def test_one(self):
        self.assertEqual(is_fibonacci_keyboard(1), "1 is in the Fibonacci sequence.")
    
if __name__ == '__main__':
    unittest.main()

