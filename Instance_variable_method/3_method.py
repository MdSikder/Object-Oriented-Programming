class Calculator:
    def add(self, x, y):
        result1 = x + y
        return print("Addition: ", result1)

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y


# Create an object of the Calculator class
my_calculator = Calculator()

# Perform calculations using the methods
# result1 = my_calculator.add(5, 3)
result2 = my_calculator.subtract(10, 4)
result3 = my_calculator.multiply(7, 2)
result4 = my_calculator.divide(9, 3)
result5 = my_calculator.divide(8, 0)  # Trying to divide by zero

# Display the results
# print("Addition: ", result1)
print("Subtraction: ", result2)
print("Multiplication: ", result3)
print("Division (9 / 3): ", result4)
print("Division (8 / 0): ", result5)

"""In this example, we have a Calculator class with four methods:

add: Adds two numbers x and y and returns the result. subtract: Subtracts y from x and returns the result. multiply: 
Multiplies x and y and returns the result. divide: Divides x by y and returns the result, but it includes a check to 
prevent division by zero. We create an object of the Calculator class, my_calculator, and then use its methods to 
perform various calculations, such as addition, subtraction, multiplication, and division. The methods encapsulate 
the logic for these operations and make it easy to perform calculations with the my_calculator object. The results 
are printed to the console.

This example demonstrates how methods can encapsulate behavior and functionality within a class, providing a way to 
perform actions or operations related to the class's concept."""
