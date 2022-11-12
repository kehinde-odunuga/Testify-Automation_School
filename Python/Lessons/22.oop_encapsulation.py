
class User:

    __first_name = "Kehinde"
    __last_name = "Odunuga"
    __attendance = 1

    def get_name(self):
        return "User-" + self.__first_name

    def get_attendance(self):
        value = self.__attendance * 20
        return value


user = User()
print(user.get_name())
print(user.get_attendance())
