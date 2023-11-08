# parent er behaviour hide korar jonne amra method overridng korte pari
# emon hote pare je parent class er kuno method amar proyojon nei ba customize dorkar
# tokhn mothod overring korte pari parent class er oi part method ta hide rakhar jonne

# method overring korar jonne child class a same method name use korte hbe

class ParentClass:  # Base class
    def method1(self):
        print("This method 1 is in ParentClass")


class ChildClass(ParentClass):  # method overriding
    def method1(self):
        print("This method 1 is in ChildClass")


# ======================================================================
ch1 = ChildClass()

# ------------
ch1.method1()
