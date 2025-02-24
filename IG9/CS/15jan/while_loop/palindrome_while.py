num = input("Enter a number: ")
reverse_num = ""
i = len(num) - 1
while i >= 0:
    reverse_num += num[i]
    i -= 1
if num == reverse_num:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
