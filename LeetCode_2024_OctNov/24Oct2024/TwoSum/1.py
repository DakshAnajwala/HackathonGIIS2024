# https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add
# up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

int_nums = []


def twosum(int_nums, target):
    foundanswer = False
    targetsum = []
    for i in range(len(int_nums)):
        for i2 in range(len(int_nums)):
            list_val1 = int_nums[i]
            list_val2 = int_nums[i2]
            if (list_val1 + list_val2 == target) and (i != i2):
                targetsum.append(i)
                targetsum.append(i2)
                print(targetsum)
                foundanswer = True
                break
        if foundanswer == True:
            break


str_nums = input("Enter a list of comma seperated numbers. ")
target = int(input("Enter your target value. "))

str_list = str_nums.split(",")
for i in str_list:
    i = int(i)
    int_nums.append(i)
twosum(int_nums=int_nums, target=target)
