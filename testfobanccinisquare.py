import unittest

class TestIsFibonacciSquare(unittest.TestCase):
    
    def test_negative_number(self):
        self.assertFalse(is_fibonacci_square(-1))
    
    def test_zero(self):
        self.assertTrue(is_fibonacci_square(0))
    
    def test_one(self):
        self.assertTrue(is_fibonacci_square(1))
    
    def test_fibonacci_square(self):
        self.assertTrue(is_fibonacci_square(144))
    
    def test_non_fibonacci_square(self):
        self.assertFalse(is_fibonacci_square(16))
    
if __name__ == '__main__':
    unittest.main()

