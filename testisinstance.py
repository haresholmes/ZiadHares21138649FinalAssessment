import unittest

class TestIsInteger(unittest.TestCase):
    
    def test_integer(self):
        self.assertTrue(is_integer(42))
    
    def test_float(self):
        self.assertFalse(is_integer(3.14))
    
    def test_string(self):
        self.assertFalse(is_integer("42"))
    
    def test_boolean(self):
        self.assertFalse(is_integer(True))
    
if __name__ == '__main__':
    unittest.main()

