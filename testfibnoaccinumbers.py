import unittest

class TestFibonacciNumbers(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(fibonacci_numbers([]), [])
    
    def test_no_fibonacci_numbers(self):
        self.assertEqual(fibonacci_numbers([2, 4, 6]), [])
    
    def test_one_fibonacci_number(self):
        self.assertEqual(fibonacci_numbers([1]), [1])
    
    def test_multiple_fibonacci_numbers(self):
        self.assertEqual(fibonacci_numbers([2, 3, 5, 8, 13]), [2, 3, 5, 8, 13])
    
    def test_mixed_list(self):
        self.assertEqual(fibonacci_numbers([1, 2, 3, 4, 5]), [1, 2, 3, 5])
    
if __name__ == '__main__':
    unittest.main()

