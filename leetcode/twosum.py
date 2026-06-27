'''
Given an array of integers nums and an integer target, return indices
 of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 '''

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    # Return an empty list if no solution is found
    return []


test_case_1 = twoSum([2,7,11,15], 9)
test_case_2 = twoSum([3,2,4], 6)
test_case_3 = twoSum([3,3], 6)


print(test_case_1)   # [0,1]
print(test_case_2)   # [1,2]
print(test_case_3)   # [0,1]