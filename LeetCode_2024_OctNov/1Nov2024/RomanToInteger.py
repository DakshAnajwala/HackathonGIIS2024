# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
# which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
#
#
#
# Example 1:
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
# Constraints:
#
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


def RomanToInt(roman):
    roman_len = len(roman)
    sum = 0
    buffer = ""
    romansplit = []
    roman.upper()
    has_more = True
    c = 0
    s = ""
    if roman == 'I' or 'V' or 'X' or 'L' or 'C' or 'D' or 'M':
        # for c in range(len(roman) -1):
        while c != roman_len:
            if roman[c] == 'I' and (roman[c + 1] == 'V' or roman[c + 1] == 'X'):
                buffer = buffer + roman[c] + roman[c + 1]
                romansplit.append(buffer)
                buffer = ""
                c += 2
            elif roman[c] == 'X' and (roman[c + 1] == 'L' or roman[c + 1] == 'C'):
                buffer = buffer + roman[c] + roman[c + 1]
                romansplit.append(buffer)
                buffer = ""
                c += 2
            elif roman[c] == 'C' and (roman[c + 1] == 'D' or roman[c + 1] == 'M'):
                buffer = buffer + roman[c] + roman[c + 1]
                romansplit.append(buffer)
                buffer = ""
                c += 2
            else:
                romansplit.append(roman[c])
                c += 1

        for r in romansplit:
            if r == 'I':
                sum += 1
            if r == 'V':
                sum += 5
            if r == 'X':
                sum += 10
            if r == 'L':
                sum += 50
            if r == 'C':
                sum += 100
            if r == 'D':
                sum += 500
            if r == 'M':
                sum += 1000
            if r == 'IV':
                sum += 4
            if r == 'IX':
                sum += 9
            if r == 'XL':
                sum += 40
            if r == 'XC':
                sum += 90
            if r == 'CD':
                sum += 400
            if r == 'CM':
                sum += 900
    return sum


roman = input("Enter Roman Number ")
print(RomanToInt(roman))
