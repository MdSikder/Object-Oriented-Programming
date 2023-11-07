"""class object constructor attributes"""


class Students:
    def __init__(self, Name, ID):
        # self means instance's property
        self.name = Name  # instance variable
        self.Id = ID  # instance variable
        # print("a Student object created")

    # instance method - instance method work by object calling
    def details(self):
        print("Name:", self.name, "ID", self.Id)


# objects
s1 = Students("Mahad Babu", 10)
s2 = Students("Karim Khan", 1)

# method calling by references to show s1 & s2 details
s1.details()
s2.details()

# value update
s1.Id = 24
s2.Id = 25

# again call to show update details
s1.details()
s2.details()
