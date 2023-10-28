""" Class Object Constructor attributes methods() """


# **************** simple non Parameterized Constructor***********************#
# blueprint / design - class
class Students1:
    pass


# objects --"variable = class_name()"
s1 = Students1()


# ************** the below code also a non Parameterized Constructor because only self in used *********************#
class Students2:
    # self contain object's address
    def __init__(self):
        # to print memory address
        print(self)
        print("a Student object created")


# here two objects made to check the different address
s2 = Students2()
s3 = Students2()
