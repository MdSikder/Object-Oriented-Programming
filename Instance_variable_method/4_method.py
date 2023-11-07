class House:
    def __init__(self):
        self.window = 4  # instance variable
        self.door = 2  # instance variable

    def view(self):
        print(self.window, "windows", self.door, "doors")


h1 = House()
h2 = House()
#  print object location
print(h1, "\n", h2)

h1.view()
h2.view()
