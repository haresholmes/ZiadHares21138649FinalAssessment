import unittest

class TestIsIntegerKeyboard(unittest.TestCase):
    
    def test_integer(self):
        self.assertEqual(is_integer_keyboard("42"), "42 is an integer.")
    
    def test_float(self):
        self.assertEqual(is_integer_keyboard("3.14"), "3.14 is not an integer.")
    
    def test_negative_integer(self):
        self.assertEqual(is_integer_keyboard("-10"), "-10 is an integer.")
    
    def test_negative_float(self):
        self.assertEqual(is_integer_keyboard("-2.5"), "-2.5 is not an integer.")
    
    def test_string(self):
        self.assertEqual(is_integer_keyboard("hello"), "hello is not an integer.")
    
if __name__ == '__main__':
    unittest.main()

