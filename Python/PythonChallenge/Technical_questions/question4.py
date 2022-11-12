
""" Question 4
# Writing  a  well-documented  code  creates  a  function  that calculates simple interest
"""

def simple_interest(P, R, T):
    I = P * R * T
    return I

calculate_simple_interest = simple_interest(500, 3, 7)

print(calculate_simple_interest)