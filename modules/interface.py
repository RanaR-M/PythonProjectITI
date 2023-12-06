from modules.regist import User


class Interface:
    def __init__(self):
        self.appface()

    @staticmethod
    def appface():
        while True:
            print("Welcome to the crowd funding library !")
            print("1)Log in\n2)Sign up\n0)Exit")
            chose = int(input("Please enter a choice: "))
            if chose == 1:
                email = User.login()
                return email
            elif chose == 2:
                User.register()
            elif chose == 0:
                break
            else:
                print("Please enter a correct choice!")
                continue



