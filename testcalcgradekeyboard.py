import unittest

def calculate_grade(correct_answers, total_questions):
    percentage = (correct_answers / total_questions) * 100
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

class TestCalculateGrade(unittest.TestCase):
    def test_grade_A(self):
        self.assertEqual(calculate_grade(9, 10), 'A')

    def test_grade_B(self):
        self.assertEqual(calculate_grade(8, 10), 'B')

    def test_grade_C(self):
        self.assertEqual(calculate_grade(7, 10), 'C')

    def test_grade_D(self):
        self.assertEqual(calculate_grade(6, 10), 'D')

    def test_grade_F(self):
        self.assertEqual(calculate_grade(5, 10), 'F')

if __name__ == '__main__':
    unittest.main()

