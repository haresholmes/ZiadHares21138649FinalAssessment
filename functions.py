def is_fibonacci(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def next_fibonacci(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b


def is_integer(n):
    return isinstance(n, int)


def fibonacci_numbers(numbers):
    fib_numbers = []
    for n in numbers:
        if is_fibonacci(n):
            fib_numbers.append(n)
    return fib_numbers


def is_square(n):
    return n >= 0 and int(n ** 0.5) ** 2 == n

def is_fibonacci_square(n):
    return is_fibonacci(n) and is_square(5 * n ** 2 + 4) or is_square(5 * n ** 2 - 4)

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

def is_fibonacci_keyboard(n):
    if is_fibonacci(n):
        return f"{n} is in the Fibonacci sequence."
    else:
        return f"{n} is not in the Fibonacci sequence."

        
def next_fibonacci_keyboard():
    n = int(input("Enter a number: "))
    if is_fibonacci(n):
        print(f"{n} is in the Fibonacci sequence.")
    else: 
        next_fibonacci = find_next_fibonacci(n)
        print(f"{n} is not in the Fibonacci sequence. The next largest number in the Fibonacci sequence after {n} is {next_fibonacci}.")



def is_integer_keyboard(n):
    try:
        int(n)
        return f"{n} is an integer."
    except ValueError:
        return f"{n} is not an integer."

def fibonacci_numbers_keyboard(numbers):
    numbers = [int(n) for n in numbers.split()]
    fib_numbers = fibonacci_numbers(numbers)
    output = "The following numbers are in the Fibonacci sequence:\n"
    for n in fib_numbers:
        output += str(n) + "\n"
    return output

def is_square_keyboard():
    n = int(input("Enter a number to check if it's a square number: "))
    if is_square(n):
        print(f"{n} is a square number.")
    else:
        print(f"{n} is not a square number.")

def is_fibonacci_square_keyboard():
    n = int(input("Enter a number to check if it's both a square number and in the Fibonacci sequence: "))
    if is_fibonacci_square(n):
        print(f"{n} is both a square number and in the Fibonacci sequence.")
    else:
        print(f"{n} is not both a square number and in the Fibonacci sequence.")

def calculate_grade_keyboard():
    correct_answers = int(input("Enter the number of correct answers: "))
    total_questions = int(input("Enter the total number of questions: "))
    grade = calculate_grade(correct_answers, total_questions)
    print(f"The grade is: {grade}")
