def add(a, b):
    c = a + b
    return c


def subtract(a, b):
    c = a - b
    return c


def multiply(a, b):
    c = a * b
    return c


def divide(a, b):
    c = a / b
    return c


a = int(input("Enter an integer value "))
b = int(input("Enter an integer value "))
operation = input("Enter the operation to be carried. \n" 
                  "+ for addition \n"
                  "- for subtraction \n"
                  "* for multiplication \n"
                  "/ for division \n")
if operation == '+':
    print(add(a=a, b=b))
elif operation == '-':
    print(subtract(a=a, b=b))
elif operation == '*':
    print(multiply(a=a, b=b))
elif operation == '/':
    print(divide(a=a, b=b))
