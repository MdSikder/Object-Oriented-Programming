# class Cat:
#     def __init__(self, color, action):
#         self.color = color
#         self.action = action
#
#     def view(self, num, clr):
#         num = num + 5
#         clr1 = clr
#         clr1[0] = "Green"
#         print("Method inside:", num)
#         print("Method inside:", clr)
#
#
# # ======================================================================================
#
# colors = ["Black", "Red", "Yellow", "Blue"]
# cl = Cat("White", "Jumping")
#
# # pass by value
# x = 55
# cl.view(x, colors)
# print("Method outside:", x)
# print("Method outside:", colors)

"""When you do clr1 = clr, you are creating a reference to the same list object as clr. This means that when you 
modify clr1, it also modifies the original clr list because they both refer to the same object in memory. Therefore, 
any changes made to clr1 are reflected in the original clr list as well.

This is why you see the same modified list in both "Method inside" and "Method outside."""

"""If you want to have different values for "Method inside" and "Method outside," you should create a copy of the clr 
list to work with inside the method without affecting the original list. You can do this using the copy method or 
slicing:"""


class Cat2:
    def __init__(self, color, action):
        self.color = color
        self.action = action

    def view(self, num, clr):
        num = num + 5
        clr1 = clr.copy()  # Creates a shallow copy of clr
        # or
        # clr1 = clr[:]  # Slicing to create a new list

        clr1[0] = "Green"
        print("Method inside:", num)
        print("Method inside:", clr)


# ======================================================================================

colors = ["Black", "Red", "Yellow", "Blue"]
cl = Cat2("White", "Jumping")

# pass by value
x = 55
cl.view(x, colors)
print("Method outside:", x)
print("Method outside:", colors)
