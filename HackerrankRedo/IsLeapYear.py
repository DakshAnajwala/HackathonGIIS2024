# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
def is_leap(year):
    # x = year / 4
    # y = year / 100
    # z = year / 400
    #
    # if x % 2 and y % 2 == 0:
    #     if z % 2 == 0:
    #         leap = True
    #     if z % 2 != 0:
    #         return False
    # else:
    #     leap = False
    #
    # # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
    else:
        return False




# year = int(input())
print(is_leap(1990))
