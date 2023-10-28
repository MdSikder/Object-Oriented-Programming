""" Class Object Constructor attributes methods() """


# **************** simple non class and objects***********************#
# blueprint / design - class
class Students1:
    pass


# objects --"variable = class_name()"
s1 = Students1()


# **************** simple class and objects with self ***********************#
class Students2:
    # self contain object's address
    def __init__(self):
        print(self)
        print("a Student object created")


# here two objects made to check the different address
s2 = Students2()
s3 = Students2()
