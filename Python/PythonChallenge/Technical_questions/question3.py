
""" Question 3
 Using the OOP feature Inheritance, create a class Animal with the method sound() and then create a Cat and Dog class that inherits from the Animal class.
 The Cat and Dog class should override the sound class and print a different sound.
"""

class Animal:
    def sound(self):
        animal_sound = "None"
        return animal_sound

class Cat(Animal):
    def sound(self):
        animal_sound = "Mew"
        return animal_sound

class Dog(Animal):
    def sound(self):
        animal_sound = "Bark"
        return animal_sound

cat_sound = Cat()
dog_sound = Dog()

print("Cat Sound:", cat_sound.sound())
print("Dog Sound:", dog_sound.sound())