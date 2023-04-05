def calculate_grade():
    correct_answers = int(input("Enter the number of correct answers: "))
    if correct_answers >= 91:
        return "Brilliant"
    elif 80 <= correct_answers < 91:
        return "Excellent"
    elif 60 <= correct_answers < 80:
        return "Great"
    elif 40 <= correct_answers < 60:
        return "Good"
    else:
        return "You can do better"

