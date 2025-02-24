def evenodd(num):
    iseven = False
    if num % 2 == 0:
        iseven = True
    else:
        iseven = False
    return iseven


num = int(input("Enter a number to check if it is even or odd. "))
print(evenodd(num=num))
