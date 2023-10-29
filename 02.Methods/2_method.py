class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking!")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")


# Creating an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Calling methods on the object
my_dog.bark()  # Calls the bark method
my_dog.eat("dog food")  # Calls the eat method

"""
In this example, we have a Dog class with three methods:

__init__: This is the constructor method, as explained in a previous response. It initializes the name and breed 
attributes when a Dog object is created.

bark: This method doesn't take any additional parameters (aside from self, which is a reference to the object itself) 
and simply prints a message indicating that the dog is barking.

eat: This method takes a food parameter and prints a message indicating that the dog is eating the specified food.

We create an object of the Dog class, my_dog, and then call its methods to make the dog bark and eat. The methods are 
called on the my_dog object, and they can access and modify the object's attributes as needed.

Methods allow objects to exhibit behavior, and they are a way to interact with and manipulate the data within those 
objects. In OOP, objects and their associated methods work together to model and simulate real-world entities and 
their actions in a structured and organized manner.

"""
