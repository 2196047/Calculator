import math


# Simple Calculator

# This function adds two variables together
def add(x, y):
    return x + y


# This function subtracts one variable from another

def subtract(x, y):
    return x - y


# This function multiplies two variables together
def multiply(x, y):
    return x * y


# This function divides one variable from another
def divide(x, y):
    return x / y


# This function gets the square of a number
def square(x):
    return x * x


# This function gets the square root of a number
def square_root(x):
    return math.sqrt(x)


# This function gets the sine of a number
def sine(x):
    return math.sin(x)


print("Choose an Operation")
print("A.Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")
print("E.Square")
print("F.Square root")
print("G.Sine")

while True:
    # Take input from a user
    operator = input("Enter choice(A/B/C/D/E/F/G): ")

    # Check if the input is valid
    if operator in ('A', 'B', 'C', 'D'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operator == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operator == 'B':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operator == 'C':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operator == 'D':
            print(num1, "/", num2, "=", divide(num1, num2))

    elif operator in ('E', 'F', 'G'):
        num1 = float(input("Enter  number: "))

        if operator == 'E':
            print(num1, "=", square(num1))

        if operator == 'F':
            print(num1, "=", square_root(num1))

        if operator == 'G':
            print(num1, "=", sine(num1))

    else:
        print("Invalid Input")
