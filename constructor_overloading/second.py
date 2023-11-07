# constructor overloading

class Student:

    # just add double * as a keyword---for work to unknown number of arguments
    def __init__(self, **info):
        if len(info) == 3:
            self.name = info["name"]
            self.Id = info["Id"]
            self.CGPA = [info["CGPA"]]
        elif len(info) == 2:
            self.name = info["name"]
            self.Id = info["Id"]
        elif len(info) == 1:
            self.name = info["name"]

        print("A Student Object created")


# =======================================================================================
# set by keyword
s1 = Student(name="carol", Id=33, CGPA=4.00)
s2 = Student(name="Bob", Id=11)
s3 = Student(name="Mike")
