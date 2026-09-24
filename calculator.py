# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b
def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

print("Welcome to Simple Calculator!")
print("Addition: ", add(5, 3))
print("Subtraction: ", subtract(10, 4))
print("Multiplication: ", multiply(4, 5))
print("Division: ", divide(10, 2))
print("Power: ", power(2, 3))
print("Modulus: ", modulus(10, 3))

