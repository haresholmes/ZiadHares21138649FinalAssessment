import unittest

class TestCalculateGrade(unittest.TestCase):
    
    def test_a_grade(self):
        self.assertEqual(calculate_grade(9, 10), 'A')
    
    def test_b_grade(self):
        self.assertEqual(calculate_grade(8, 10), 'B')
    
    def test_c_grade(self):
        self.assertEqual(calculate_grade(7, 10), 'C')
    
    def test_d_grade(self):
        self.assertEqual(calculate_grade(6, 10), 'D')
    
    def test_f_grade(self):
        self.assertEqual(calculate_grade(5, 10), 'F')
    
    def test_zero_questions(self):
        self.assertEqual(calculate_grade(5, 0), 'F')
    
    def test_negative_answers(self):
        self.assertEqual(calculate_grade(-1, 10), 'F')
    
    def test_negative_questions(self):
        self.assertEqual(calculate_grade(5, -1), 'F')
    
if __name__ == '__main__':
    unittest.main()

