
""" Question 6
# Write  a  function  that  removes  repeated  characters from a string. Sample Strings are: a. Hello: output shouldbe Helo b. Concatenate: output should be Conatent
"""
from collections import OrderedDict

def removeDuplicate(string):
    return "".join(OrderedDict.fromkeys(string))


print(removeDuplicate("hello"))
print(removeDuplicate("concatenate"))
print(removeDuplicate("testify"))
print(removeDuplicate("automation"))
print(removeDuplicate("committee"))