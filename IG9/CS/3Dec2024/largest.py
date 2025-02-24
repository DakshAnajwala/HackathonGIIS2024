def largest(a, b):
    largest = 0
    a = int(a)
    b = int(b)
    if a > b:
        largest = a
    elif a < b:
        largest = b
    return largest


a = int(input("Enter an integer value "))
b = int(input("Enter an integer value "))
print(largest(a=a,b=b))
