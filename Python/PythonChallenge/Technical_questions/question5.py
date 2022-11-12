""" Question 5
# Write  a  Python  program  that  checks  if  a  string  is  a palindrome,  Then  optionally  write  a  unit  test  to  check  your program's correctness.
"""

"""def is_palindrome(string):
    palindrome = ''.join(reversed(string))

    if string == palindrome:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

string1 = "level"
is_palindrome(string1)

string2 = "automation"
is_palindrome(string2)

string3 = "madam"
is_palindrome(string3) """

# Unit Test
def is_palindrome(string):
    return ''.join(reversed(string))

#def test_is_palindrome():
    #assert is_palindrome("level") == "level"

def test_is_palindrome():
    assert is_palindrome("automation") != "automation"

def test_is_palindrome():
    assert is_palindrome("madam") == "madam"