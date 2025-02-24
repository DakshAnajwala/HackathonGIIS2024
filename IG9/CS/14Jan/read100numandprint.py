nums = []
for i in range(100):
    n = int(input("Enter a number "))
    nums.append(n)

for num in nums:
    if num%2 == 0:
        even_count = even_count + 1
        even_sum = even_sum + num
    if num%2 != 0:
        odd_count = odd_count + 1
        odd_sum = odd_sum + num


