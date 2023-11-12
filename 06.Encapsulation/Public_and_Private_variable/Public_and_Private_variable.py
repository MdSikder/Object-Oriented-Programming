class Student:
    def __init__(self, name, Id):
        self.name = name  # instance variable
        self.__Id = Id  # private instance variable

    def details(self):
        print("Name:", self.name, "," "ID:", self.__Id)


# =============================================================
s1 = Student("Bob", 11)
s2 = Student("Carol", 24)
# s1.__Id = -66       # try to update id, that is not possible because of private
# print(s1.__dict__)  # to check update or not, after run you can 's1.__Id = -66' is work like a new instance variable

s1.details()
s2.details()
