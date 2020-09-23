# Program make a simple calculator


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Choose an Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    operator = input("Enter choice(A/B/C/D): ")

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
