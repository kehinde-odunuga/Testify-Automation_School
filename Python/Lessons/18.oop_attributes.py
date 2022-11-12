
# class
class Animal:

    group = "Mammal"
    can_walk = True

    def __init__(self, name):
        self.name = name


cat = Animal("Cat")
dog = Animal("Dog")

print(cat.name)
print(dog.name)

print(cat.group)
print(dog.group)