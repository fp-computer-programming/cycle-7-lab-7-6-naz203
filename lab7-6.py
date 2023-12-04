"""
Create a Python file named lab_7-6.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a 2 separate functions within the same document. 
Create a 3rd function which requires both the first two functions within it
Create 4 test cases for your 3rd function. 
"""
# Function to add two numbers
def add_numbers(a, b):
    return a + b


# Function to multiply two numbers
def multiply_numbers(a, b):
    return a * b


# Function that requires both add_numbers and multiply_numbers
def combine_operations(x, y, z):
    result_sum = add_numbers(x, y)
    result_product = multiply_numbers(result_sum, z)
    return result_product


# Test cases for combine_operations
test_case_1 = combine_operations(2, 3, 4)  # (2 + 3) * 4 = 20
test_case_2 = combine_operations(5, 2, 1)  # (5 + 2) * 1 = 7
test_case_3 = combine_operations(-1, 7, 2)  # (-1 + 7) * 2 = 12
test_case_4 = combine_operations(0, 0, 10)  # (0 + 0) * 10 = 0


print(test_case_1, test_case_2, test_case_3, test_case_4)
