import unittest

class TestNextFibonacciKeyboard(unittest.TestCase):
    
    def test_fibonacci_number(self):
        self.assertEqual(next_fibonacci_keyboard(5), "5 is in the Fibonacci sequence.")
    
    def test_non_fibonacci_number(self):
        self.assertEqual(next_fibonacci_keyboard(6), "6 is not in the Fibonacci sequence. The next largest number in the Fibonacci sequence after 6 is 8.")
    
    def test_negative_number(self):
        self.assertEqual(next_fibonacci_keyboard(-1), "-1 is not in the Fibonacci sequence. The next largest number in the Fibonacci sequence after -1 is 0.")
    
    def test_zero(self):
        self.assertEqual(next_fibonacci_keyboard(0), "0 is in the Fibonacci sequence.")
    
    def test_one(self):
        self.assertEqual(next_fibonacci_keyboard(1), "1 is in the Fibonacci sequence.")
    
if __name__ == '__main__':
    unittest.main()

