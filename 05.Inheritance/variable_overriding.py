class Animal:
    def __init__(self, name):
        self.name = name
        self.color = "White"

    def eat(self):
        print(self.color, self.name, "is eating")


# ========================================================
class Dog(Animal):
    # ekhane 'color' ta variable overriding kora hoyeche, onnothai always
    # color 'white' print korto
    def __init__(self, name, color):
        super().__init__(name)  # to inherit parent __init__ method
        self.color = color      # manually set kore diyechi

    def bark(self):
        print(self.color, self.name, "is barking")


# ========================================================
d1 = Dog("Rover", "Brown")
d1.bark()

print(d1.__dict__)  # to check overriding
