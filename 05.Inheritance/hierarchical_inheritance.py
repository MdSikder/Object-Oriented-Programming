# One single class -> multiple child class

class ParentClass:  # Base class
    def method1(self):
        print("This method 1 is in ParentClass")


class ChildClass1(ParentClass):  # Derived Class 1
    def method2(self):
        print("This method 2 is in ChildClass 2")


class ChildClass2(ParentClass):  # Derived Class 2
    def method3(self):
        print("This method 3 is in ChildClass 2")


# ======================================================================
ch1 = ChildClass1()
ch2 = ChildClass2()
# ------------
ch1.method1()
ch1.method2()
# --------
ch2.method1()
ch2.method3()
