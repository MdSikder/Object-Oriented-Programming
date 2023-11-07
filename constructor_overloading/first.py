# constructor overloading

class Student:

    def __init__(self, *info):
        if len(info) == 3:
            self.name = info[0]
            self.Id = info[2]
            self.CGPA = [3]
        elif len(info) == 2:
            self.name = info[0]
            self.Id = info[1]
        elif len(info) == 1:
            self.name = info[0]

        print("A Student Object created")


# =======================================================================================
s1 = Student("carol", 33, 4.00)
s2 = Student("Bob", 11)
s3 = Student("Mike")
