import re
from modules.handling_functions import save_user, get_user

class User:
    def __init__(self):
        pass

    @staticmethod
    def register():
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        while True:
            print("Please enter the following data.")
            First_Name = input("Your first name: ")
            if First_Name.isalpha():
                while True:
                    Last_Name = input("Your last name: ")
                    if Last_Name.isalpha():
                        while True:
                            email = input("Email: ")
                            if re.fullmatch(email_regex, email):
                                while True:
                                    Password = input("Password: ")
                                    if len(Password) >= 8:
                                        while True:
                                            Confirm_Password = input("Confirm Password: ")
                                            if Confirm_Password == Password:
                                                while True:
                                                    Phone = input("Your Phone Number: ")
                                                    if (Phone.isdigit()
                                                            and len(Phone) == 11
                                                            and (Phone.startswith("011") | Phone.startswith(
                                                                "012") | Phone.startswith("010") | Phone.startswith(
                                                                "015"))):
                                                        print("You have completed the registration.")
                                                        data = {'firstname': [First_Name], 'lastname': [Last_Name],
                                                                'email': [email],
                                                                'password': [Password], 'phone': [Phone]}
                                                        save_user(data)
                                                        break
                                                    else:
                                                        print("Please enter valid phone number!")
                                                break
                                            else:
                                                print("Password not match!")
                                        break
                                    else:
                                        print("Password length must 8 or more!")
                                break
                            else:
                                print("Please enter valid email")
                        break
                    else:
                        print("Please enter last name without number!")
                break
            else:
                print("Please enter first name without number!")

    @staticmethod
    def login():
        while True:
            email = input("Email: ")
            password = input("Password: ")
            check_data = get_user(email, password)
            if check_data:
                return email
            else:
                print('Wrong password')
