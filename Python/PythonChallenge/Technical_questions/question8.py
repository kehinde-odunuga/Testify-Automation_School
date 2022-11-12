
""" Question 8
# Create a program that prints out the even numbers in an array. Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,401, 0 ]
"""

def num_array1(numbers):
    # iteration
    for number in numbers:

        # check for remainder
        if number % 2 == 0:
            print(number)

def num_array2(numbers):
    # iteration
    for number in numbers:

        # check for remainder
        if number % 2 == 0:
            print(number)

num_array1([1, 2, 3, 4, 5, 6])
num_array2([ 34, 2, 9, 91, 19, 401, 0 ])


