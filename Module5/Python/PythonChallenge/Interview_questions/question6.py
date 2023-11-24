
# Question 6
# Of the available unit test framework in Python, which is your favorite and why.

# Pytest is my favourite. It is an all-purpose testing framework and easy to use.

def test_addition():
    assert bodmas.addition(3, 1) == 4
    assert bodmas.addition(5, 3) == 8
    assert bodmas.addition(30, 11) != 4

def test_substraction():
    assert bodmas.subtraction(20, 10) == 10
    assert bodmas.subtraction(1, 2) == -1
    assert bodmas.subtraction(50, 10) != 10