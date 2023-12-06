from modules import handling_functions as f
from modules.interface import Interface


email = Interface.appface()
if email is not None:
    number = 0
    while number != 6:
        number = f.get_number(email)
        f.handel_orders(number, email)
else:
    print('Goodbye !!')

