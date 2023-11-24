
# Module 3b Task 19

# 1. Create a class called Human
# 2. Add an attribute leg_count with the value of 4
# 3. Add another attribute can_walk with the value of True
# 4. Create a method called get_description, the method should print "This is human"
# 5. Create another method that return the leg count, the name of the method is your choice
#=> Optionally you can instantiate the class and invoke the method get_description() and invoke your method that returns leg count.

class Human:
    leg_count = 4
    can_walk = True

    def __init__(self):
        self.name = "Kehinde"

    def get_description(self):
        if self.name == "Kehinde":
            print("This is human")

    def get_description(self):
        if self.name == "Kehinde":
            print("This is human")

human = Human()
human.get_description()

print("Human:", human.leg_count)


