"""class object constructor attributes"""


class Students:
    def __init__(self, Name, ID):
        # self means instance's property
        self.name = Name  # instance variable
        self.Id = ID  # instance variable
        print("a Student object created")


# objects
s1 = Students("Mahad Babu", 10)
s2 = Students("Karim Khan", 1)

# before s1 means reference call from objectt
print(s1.name, s1.Id)
print(s2.name, s2.Id)

# now update ID
s1.Id = 33
print(s1.name, s1.Id)
