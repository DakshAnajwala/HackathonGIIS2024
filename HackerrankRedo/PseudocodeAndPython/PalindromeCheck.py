# Write a pseudocode to check if the given number is palindrome or not
num = input("Enter a number to check if it is palindrome or not ")
if num[::-1] == num:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")