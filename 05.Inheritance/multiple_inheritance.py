# jokhn ekta class a multiple parents thakbe

class ParentClass1:  # Base class 1
    def method1(self):
        print("This method 1 is in ParentClass 1")


class ParentClass2:  # Base class 2
    def method2(self):
        print("This method 2 is in ParentClass 2")


class ChildClass(ParentClass1, ParentClass2):  # Derived Class 1
    def method3(self):
        print("This method 3 is in ChildClass")


# ======================================================================
ch1 = ChildClass()

# ------------
ch1.method1()
ch1.method2()
ch1.method3()
