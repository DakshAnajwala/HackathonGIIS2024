'''
print a series  like
1
22
333
4444

and
1
12
123
1234


     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5
'''

tri_string = ""
skibidi = len(tri_string)
stop = int(input("Enter when the last digit of the triangle and be skibidi "))
for i in range(stop):
    tri_string = ""
    if len(tri_string) < (i+1):
        for i in range(i):
            tri_string = tri_string + str(i+1)
        print(tri_string)



