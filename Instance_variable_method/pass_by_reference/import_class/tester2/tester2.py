# from folder_name import class_name
from Instance_variable_method.pass_by_reference.import_class import book

b1 = book.Book("Rupa", "Humayun Ahmed")
b1.set_price(299)
print(b1.get_price())
b1.details()
