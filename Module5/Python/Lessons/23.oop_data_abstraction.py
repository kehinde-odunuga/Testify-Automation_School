
class LoginSession:

    __email = "kehinde@test.com"
    __password = "password"

    def get_email(self):
        return self.__email

    def get_password(self):
        return "********"

session = LoginSession()
print(session.get_email())
print(session.get_password())