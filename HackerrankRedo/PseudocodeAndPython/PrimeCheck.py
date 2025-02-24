# Write a pseudocode to check if the given number is prime or not


if __name__ == "__main__":
    num = int(input("Enter a number to check if it is prime or not "))
    if num <= 1:
        print(f"Since your given number, {num}, is less than or equal to 1, it cannot have any prime numbers.")
    for i in range(num):
        primecheck = i + 2
        if (num - 1) == primecheck and num % primecheck != 0:
            print(f"The given number, {num} is a prime number")
        if num % primecheck == 0:
            print(f"The given number, {num} is not a prime number")
            break

