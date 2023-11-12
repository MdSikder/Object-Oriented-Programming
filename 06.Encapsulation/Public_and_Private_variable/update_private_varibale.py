class Student:
    def __init__(self, name, Id):
        self.name = name  # instance variable
        self.__Id = Id  # private instance variable

    def details(self):
        print("Name:", self.name, "," "ID:", self.__Id)

    def updt_id(self, Id):
        if Id > 0:    # here variable make encapsulate
            self.__Id = Id
        else:
            print("Invalid ID, enter again")


# =============================================================
s1 = Student("Bob", 11)
s2 = Student("Carol", 24)
s1.updt_id(-666)    # it is encapsulation

s1.details()
s2.details()
