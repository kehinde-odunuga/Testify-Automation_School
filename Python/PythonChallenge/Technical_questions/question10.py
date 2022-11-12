
""" Question 10
# Create a function that converts any string value to a Sentence  case,  Then  write  a  unit  test  that  checks  the function's correctness.
"""

"""
def sentence_case(sentence):
    sentence = "quality assurance engineer"
    conversion = sentence.capitalize()
    print(conversion) 

sentence_case()
"""
# Unit Test
def sentence_case(sentence):
    return sentence.capitalize()

def test_sentence_case():
    assert sentence_case("quality assurance engineer") == "Quality assurance engineer"