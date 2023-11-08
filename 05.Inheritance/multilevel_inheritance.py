class ParentClass:  # Base class
    def method1(self):
        print("This method 1 is in ParentClass")


class ChildClass(ParentClass):  # Derived Class 1
    def method2(self):
        print("This method 2 is in ChildClass")


class ChildClass2(ChildClass):  # Derived Class 2
    def method3(self):
        print("This method 3 is in ChildClass")


# ======================================================================
ch2 = ChildClass2()
ch2.method1()
ch2.method2()
ch2.method3()
