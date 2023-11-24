
# Module 3b Task 17

# Create a class called Human
# instantiate the class

class Human:

    name = "Kehinde"
    group = "Black"

    def get_name_group(self):
        return self.name + ":" + self.group


# object
boy = Human()
print(boy.name, boy.group, boy.get_name_group())
