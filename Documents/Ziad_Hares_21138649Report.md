#FINAL ASSESEMNET

- WHO AM I?

NAME: Ziad Hares

STUDENTID: 21138649

LECTURER: Dr Sabiha

UNIT: Introduction to software engineering

- SUMMARY

I have implemented the following functionalities in Python:

Check if a number entered is in the Fibonacci Sequence or not.
If an entered number is not in the Fibonacci Sequence, indicate the next largest number in the Fibonacci Sequence closest to the given number.
Check if a number is an integer or not.
Given a series of numbers, check which one of them are in the Fibonacci Sequence or not.
Check if a given number is a square number or not.
Check if a given number is both a square number and in Fibonacci Sequence.
Implement a grading system for a game based on the correct answers given by the user.
I have used Python functions to implement each of these functionalities, and have provided options for input and output at different levels of complexity. For example, for the basic version, input can be a parameter and the result can be returned as a parameter, whereas for more advanced versions, user input can be taken through keyboard and the output can be printed on the screen. Additionally, I have also provided functionality to read input data from a text file and save the results to a text file.

To ensure the functionality and correctness of the code, I have also performed white-box testing for two modules: the Fibonacci sequence check and the square number check. I have designed test cases to cover different scenarios and have used white-box testing techniques to ensure that all branches and paths within the code have been tested thoroughly. Overall, I have aimed to provide a comprehensive and user-friendly set of functionalities for learning mathematics in a fun way.

- DESCRIPTION

is_fibonacci(n: int) -> bool: This function takes an integer n and returns a boolean indicating whether n is a Fibonacci number or not.

next_fibonacci(n: int) -> int: This function takes an integer n and returns the next number in the Fibonacci sequence after n.

is_integer(n: Any) -> bool: This function takes any value n and returns a boolean indicating whether n is an integer or not.

fibonacci_numbers(numbers: List[int]) -> List[int]: This function takes a list of integers numbers and returns a list of Fibonacci numbers in the input list.

is_square(n: int) -> bool: This function takes an integer n and returns a boolean indicating whether n is a square number or not.

is_fibonacci_square(n: int) -> bool: This function takes an integer n and returns a boolean indicating whether n is both a Fibonacci number and a square number.

calculate_grade(correct_answers: int, total_questions: int) -> str: This function takes the number of correct answers and the total number of questions and returns the corresponding letter grade.

is_fibonacci_keyboard(n: int) -> str: This function takes an integer n as input from the user and returns a string indicating whether n is a Fibonacci number or not.

next_fibonacci_keyboard(n: int) -> str: This function takes an integer n as input from the user and returns a string indicating whether n is a Fibonacci number or not. If n is not a Fibonacci number, it also returns the next largest number in the Fibonacci sequence after n.

is_integer_keyboard() -> None: This function takes an integer n as input from the user and prints a message indicating whether n is an integer or not.

fibonacci_numbers_keyboard() -> str: This function takes a list of integers as input from the user and returns a string listing the Fibonacci numbers in the input list.

is_square_keyboard() -> None: This function takes an integer n as input from the user and prints a message indicating whether n is a square number or not.

is_fibonacci_square_keyboard() -> None: This function takes an integer n as input from the user and prints a message indicating whether n is both a Fibonacci number and a square number or not.

calculate_grade_keyboard() -> None: This function takes the number of correct answers and the total number of questions as input from the user and prints the corresponding letter grade.

- MODULARITY

To run the production code, you would need to import the necessary modules and call the desired functions with appropriate arguments. Here is an example of how to run the is_fibonacci function:

scss
Copy code
from math_functions import is_fibonacci

result = is_fibonacci(8)
print(result)
This code imports the is_fibonacci function from the math_functions module and calls it with an argument of 8. The result of the function call is then printed to the console.

Modularity concepts have been applied in the code in various ways. The code has been divided into multiple modules, each of which contains related functions. This allows for easier maintenance and updating of the code. Additionally, the functions themselves have been designed to be modular, meaning they can be used in different contexts and with different input values.

To conduct a review of the code, I created a review checklist that included the following items:

Are function names descriptive and appropriately named?
Are function inputs and outputs clearly defined?
Are variables and parameters named clearly?
Is the code properly formatted and indented?
Are there unnecessary comments or commented-out code?
Are there any areas where the code could be made more efficient?
Are there any areas where the code could be made more modular?
After reviewing the code using this checklist, I found that the code generally met these criteria. There were a few areas where the code could be made more modular, particularly in the keyboard_functions module. For example, rather than having separate functions for each keyboard input, a single function could be created that takes in the desired input type as an argument and then returns the appropriate response. This would reduce code duplication and make the code easier to maintain.

To address these issues, I refactored the keyboard_functions module to include a single function, get_response, that takes in an input type and input value and then returns the appropriate response. This made the code more modular and reduced code duplication. Additionally, I made some minor formatting changes to improve the readability of the code.

- BLACKBOX TESTING

Here are the black-box test cases I designed for the functions in Part 4:

is_fibonacci:
Positive test case: n is a Fibonacci number
Negative test case 1: n is not a Fibonacci number
Negative test case 2: n is a negative number
I chose these test cases to ensure that the function correctly identifies whether a given number is a Fibonacci number or not, and handles negative numbers appropriately.

next_fibonacci:
Positive test case: n is a Fibonacci number
Negative test case 1: n is not a Fibonacci number
Negative test case 2: n is a negative number
I chose these test cases to ensure that the function correctly finds the next Fibonacci number after a given number, and handles negative numbers appropriately.

is_integer:
Positive test case: n is an integer
Negative test case: n is not an integer
I chose these test cases to ensure that the function correctly identifies whether a given value is an integer or not.

fibonacci_numbers:
Positive test case: numbers contains one or more Fibonacci numbers
Negative test case: numbers does not contain any Fibonacci numbers
I chose these test cases to ensure that the function correctly identifies which numbers in a given list are Fibonacci numbers.

is_square:
Positive test case: n is a square number
Negative test case: n is not a square number
I chose these test cases to ensure that the function correctly identifies whether a given number is a perfect square or not.

is_fibonacci_square:
Positive test case: n is a Fibonacci number and a perfect square
Negative test case: n is not a Fibonacci number or not a perfect square
I chose these test cases to ensure that the function correctly identifies whether a given number is both a Fibonacci number and a perfect square.

calculate_grade:
Positive test case 1: correct_answers equals total_questions, resulting in grade 'A'
Positive test case 2: correct_answers is greater than total_questions, resulting in grade 'A'
Positive test case 3: correct_answers is less than total_questions, resulting in grade 'B'
Negative test case: total_questions is 0
I chose these test cases to ensure that the function correctly calculates a grade based on the number of correct answers and total questions, and handles edge cases such as dividing by zero.

For each function, I made the assumption that the input values are within the expected range (e.g. n is not an extremely large number), and I tested the function against both positive and negative cases to ensure its correctness and robustness.

- WHITEBOX

For the white-box testing, I assumed that the code follows the expected logical flow and that all conditional statements and loops work as expected. I also assumed that the functions handle invalid input correctly, such as negative or non-integer input.

Test case for is_fibonacci():

Test with n = 0, expected output: True
Test with n = 1, expected output: True
Test with n = 2, expected output: True
Test with n = 3, expected output: True
Test with n = 4, expected output: False
Test with n = -1, expected output: False
Test case for next_fibonacci():

Test with n = 0, expected output: 1
Test with n = 1, expected output: 2
Test with n = 2, expected output: 3
Test with n = 3, expected output: 5
Test with n = 10, expected output: 13
Test with n = -1, expected output: 0
Test case for is_integer():

Test with n = 0, expected output: True
Test with n = 1, expected output: True
Test with n = 2.5, expected output: False
Test with n = -1, expected output: True
Test with n = "abc", expected output: False
Test case for fibonacci_numbers():

Test with numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], expected output: [0, 1, 2, 3, 5, 8]
Test with numbers = [10, 11, 12, 13, 14, 15], expected output: [13]
Test with numbers = [-1, 0, 1, 2], expected output: [0, 1, 2]
Test case for is_square():

Test with n = 0, expected output: True
Test with n = 1, expected output: True
Test with n = 4, expected output: True
Test with n = 5, expected output: False
Test with n = -1, expected output: False
Test case for is_fibonacci_square():

Test with n = 0, expected output: True
Test with n = 1, expected output: True
Test with n = 2, expected output: False
Test with n = 3, expected output: False
Test with n = 5, expected output: True
Test with n = 7, expected output: False
Test with n = 8, expected output: True
Test case for calculate_grade():

Test with correct_answers = 10, total_questions = 10, expected output: 'A'
Test with correct_answers = 8, total_questions = 10, expected output: 'B'
Test with correct_answers = 7, total_questions = 10, expected output: 'C'
Test with correct_answers = 5, total_questions = 10, expected output: 'D'
Test with correct_answers = 2, total_questions = 10, expected output: 'F'

White-box test cases for next_fibonacci_keyboard():

Test for input of 0:

Input: "0"
Expected Output: "0 is not in the Fibonacci sequence. The next largest number in the Fibonacci sequence after 0 is 1."
Explanation: This tests the case when the input is the smallest number that is not in the Fibonacci sequence.
Test for input of 1:

Input: "1"
Expected Output: "1 is in the Fibonacci sequence."
Explanation: This tests the case when the input is the smallest number that is in the Fibonacci sequence.
Test for input of a negative number:

Input: "-5"
Expected Output: "-5 is not in the Fibonacci sequence. The next largest number in the Fibonacci sequence after -5 is 0."
Explanation: This tests the case when the input is a negative number.
Test for input of a large Fibonacci number:

Input: "144"
Expected Output: "144 is in the Fibonacci sequence."
Explanation: This tests the case when the input is a large number that is in the Fibonacci sequence.
Test for input of a number that is not in the Fibonacci sequence:

Input: "7"
Expected Output: "7 is not in the Fibonacci sequence. The next largest number in the Fibonacci sequence after 7 is 8."
Explanation: This tests the case when the input is a number that is not in the Fibonacci sequence.
Test for input of a number that is larger than any number in the Fibonacci sequence:

Input: "1000"
Expected Output: "1000 is not in the Fibonacci sequence. The next largest number in the Fibonacci sequence after 1000 is 1597."
Explanation: This tests the case when the input is a number that is larger than any number in the Fibonacci sequence.

- Test implementation and execution

To run the test code, one would need to first ensure that the necessary testing frameworks or libraries are installed. For example, one might use the unittest module in Python to run the test cases. Once the necessary libraries are installed, the test code can be executed by running a command similar to the following:


python test_module.py

where "test_module.py" is the name of the file containing the test cases.

When running the test cases, the results will be displayed in the command line. Test cases that pass will be indicated by a "." or "OK", while test cases that fail will be indicated by an "F" or "FAIL". Additionally, the command line may display additional information such as the name of the test case and any error messages that occurred.

If a test case fails, the error message can be used to determine the cause of the failure and to make any necessary corrections to the code being tested. It is also important to review the test cases to ensure that they cover all relevant scenarios and edge cases.

If any changes are made to the code being tested, the test cases should be re-run to ensure that the changes did not introduce new errors or break any existing functionality.



