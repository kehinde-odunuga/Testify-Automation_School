
# Module 3b Task 21

# 1. Create a class called Human
# 2. Add an attribute leg_count with the value of 4
# 3. Add a method called get_gender() that returns "Unknown" in the Human class
# 4. Create another class called Man that extends Human
# 5. Create another class called Woman that extends Human
# 6. In the class, Man create the method get_gender() which should return "man"
# 7. In the class, Woman create the method get_gender() which should return "woman"
# 8. Instantiate the Man and Woman classes
# 9. Print out the value of get_gender() from the Man and Woman object instances

class Human:
    leg_count = 4

    def get_gender(self):
        print("Gender: Unknown")

class Man(Human):

    def get_gender(self):
        print("Gender: Man")

class Woman(Human):

    def get_gender(self):
        print("Gender: Woman")


man = Man()
man.get_gender()

woman = Woman()
woman.get_gender()
