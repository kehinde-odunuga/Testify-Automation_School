
# Module 3b Task 25

# 1. Create a class called Utilities
# 2. Create a static method called print_name which accepts a parameter, and prints out the parameter.
# 3. Invoke the static method print_name()
# 4. You can use any of the two methods to create your static methods.

class Utilities:

    @staticmethod
    def print_name(self):
        return self

utilities = Utilities()
print(utilities.print_name("Water"))



