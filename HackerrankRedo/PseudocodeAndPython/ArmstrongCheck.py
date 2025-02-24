# Write a pseudocode to check if the given number is armstrong or not
if __name__ == "__main__":
    num = (input("Enter a number to check if it is armstrong or not "))
    arm_digit = 0
    sum = 0
    for i in num:
        i = int(i)
        arm_digit = i**3
        sum = sum + arm_digit
    if sum == int(num):
        print(f"The given number, {num} is an armstrong number")

    else:
        print(f"The given number, {num} is not an armstrong number")
