
""" Question 3
Create  a  function  that  calculates  the  power  of  a  number. Then  write  a  unit  test  to  check  the  correctness  of  the function
"""

def CalculatePower(X, N):
    return X ** N
    # X is the base, while N is the power

#print(pow(5, 3))



def test_CalculatePower():
    assert CalculatePower(5, 3) == 125