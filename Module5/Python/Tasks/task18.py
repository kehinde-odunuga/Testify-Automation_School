
# Module 3b Task 18

# Create a class called Human
# Add an attribute leg_count with the value of 4
# Add an attribute can_walk with the value of True
# Optionally you can instantiate the class and print out the leg_count and can_walk attributes

class Human:

    leg_count = 4
    can_walk = True

    def __init__(self, name):
        self.name = name

boy = Human("Kehinde")

print(boy.name)
print(boy.leg_count)
print(boy.can_walk)
