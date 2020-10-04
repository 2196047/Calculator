import math


#Simple Calculator

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


def squareRoot(x):
    return math.sqrt(x)

def sine(x):
    return math.sin(x)


def sine(x):
    return math.sin(x)

print("Choose an Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    # Take input from a user
    operator = input("Enter choice(A/B/C/D): ")

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
        break
    else:
        print("Invalid Input")
