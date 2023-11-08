class ParentClass:  # Base class
    def method1(self):
        print("This method 1 is in ParentClass 1")


class ChildClass1(ParentClass):  # Derived Class 1
    def method2(self):
        print("This method 2 is in ChildClass 1")


class ChildClass2(ChildClass1):  # Derived Class 2
    def method3(self):
        print("This method 3 is in ChildClass 2")


class ChildClass3(ChildClass1):  # Derived Class 2
    def method4(self):
        print("This method 4 is in ChildClass 3")


# ======================================================================
ch3 = ChildClass3()
ch2 = ChildClass2()
ch1 = ChildClass1()

# ------------
ch3.method1()
ch3.method2()
ch3.method4()

ch2.method1()
ch2.method2()
ch2.method3()

ch1.method1()
ch1.method2()
