class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action

    def view(self):
        print(self.color, "cat is", self.action)

    def compare(self, ct):
        if self.action == ct.action:
            print("Both cats are ", self.action)
        else:
            print("They are different")


# ======================================================================================

