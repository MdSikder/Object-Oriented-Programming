class Car:
    def __init__(self, Name, Model):
        self.name = Name  # instance Variable
        self.model_Year = Model  # instance Variable
        self.wheel = 4  # instance Variable

    def view(self):
        print("The name of the car is : ", self.name, "\n" "The model year of this : ", self.model_Year, "\n" "It is", self.wheel, "wheel car \n")


# -------------------------------------------------------------------
c1 = Car("BMW", 2012)
c2 = Car("ODI", 2016)

# update wheel
c2.wheel = 6
c1.view()
c2.view()
