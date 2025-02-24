num = input("Enter a number: ")
reverse_num = ""
for digit in num:
    reverse_num = digit + reverse_num
if num == reverse_num:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
