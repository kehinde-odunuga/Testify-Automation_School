
"""  Question 9
# Create  a  function  that  converts  any  string  value  to  uppercase,  Then  write  a  unit  test  that  checks  the  function's correctness
"""

def is_upper(string):
    return string.upper()

upper_case = is_upper("it is easy to code with python")
print("Upper Case:", upper_case)


# Unit Test
def is_upper(string):
    return string.upper()

def test_is_upper():
    assert is_upper("quality assurance engineer") == "QUALITY ASSURANCE ENGINEER"