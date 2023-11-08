class ParentClass:  # Base class
    def method1(self):
        print("This method1 is in ParentClass")

    def method2(self):
        print("This method2 is in ParentClass")


class ChildClass(ParentClass):  # Derived Class
    def method3(self):
        print("This is method 3 is in ChildClass")


# ======================================================================
ch1 = ChildClass()
ch1.method1()
ch1.method2()
ch1.method3()
