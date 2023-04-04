import unittest

class TestFibonacci(unittest.TestCase):
    
    def test_negative_number(self):
        self.assertFalse(is_fibonacci(-1))
    
    def test_zero(self):
        self.assertTrue(is_fibonacci(0))
    
    def test_one(self):
        self.assertTrue(is_fibonacci(1))
    
    def test_small_fibonacci_number(self):
        self.assertTrue(is_fibonacci(5))
    
    def test_large_fibonacci_number(self):
        self.assertTrue(is_fibonacci(6765))
    
    def test_non_fibonacci_number(self):
        self.assertFalse(is_fibonacci(4))
    
if __name__ == '__main__':
    unittest.main()

