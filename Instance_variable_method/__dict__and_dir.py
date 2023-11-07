# create dog with name and color
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update_color(self, color):
        self.color = color

    def poke(self):
        print(self.color, self.name, "is smiling")


# =======================================================================================
d1 = Dog("rover", "Brown")
d2 = Dog("tomy", "white")
d1.poke()
d2.poke()
# update color
d1.update_color("Black")
# check updated dog
d1.poke()
# update color
d1.update_color("Red")
# check updated dog
d1.poke()
# ==================use __dict__ call to show attribute value=======================
print(d1.__dict__)
print(d2.__dict__)

# ==================use dir() call to show object details=======================
print(dir(d1))
print(dir(d2))
