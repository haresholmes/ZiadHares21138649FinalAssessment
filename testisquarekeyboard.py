import unittest
from io import StringIO
from unittest.mock import patch

class TestIsSquareKeyboard(unittest.TestCase):
    
    def test_is_square_keyboard(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value='16'):
                is_square_keyboard()
                self.assertEqual(fake_output.getvalue().strip(), '16 is a square number.')
            
            with patch('builtins.input', return_value='25'):
                is_square_keyboard()
                self.assertEqual(fake_output.getvalue().strip(), '25 is a square number.')
                
            with patch('builtins.input', return_value='12'):
                is_square_keyboard()
                self.assertEqual(fake_output.getvalue().strip(), '12 is not a square number.')
                
            with patch('builtins.input', return_value='0'):
                is_square_keyboard()
                self.assertEqual(fake_output.getvalue().strip(), '0 is a square number.')
                
            with patch('builtins.input', return_value='-5'):
                is_square_keyboard()
                self.assertEqual(fake_output.getvalue().strip(), '-5 is not a square number.')
                
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

