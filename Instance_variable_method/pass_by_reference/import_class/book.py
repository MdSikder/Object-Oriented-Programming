# Make book with name author and price
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0

    # get set method naming convention good to use
    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def details(self):
        print("Book Name:", self.name, "\nAuthor:", self.author, "\nPrice:", self.price, "Taka")


# =======================================================================================
# b1 = Book("Rupa", "Humayun Ahmed")
# b1.details()
# b1.set_price(260)
# b1.details()
# print(b1.get_price())
