#importing some_rando and make_messages function from py_day_test file
from py_day_test import some_rando, make_messages 
#importing MessageUser class from make_messages file inside py_day_mod folder
from py_day_mod.make_messages import MessageUser

obj = MessageUser()
obj.add_user("Abc", 123.32, email='hello@teamcfe.com')
obj.add_user("jOhn", 94.23)
obj.add_user("Sean", 93.23)
obj.add_user("Emilee", 193.23)
obj.add_user("Marie", 13.23)
obj.get_details()

print(obj.make_messages())
default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

make_messages(default_names, default_amounts)