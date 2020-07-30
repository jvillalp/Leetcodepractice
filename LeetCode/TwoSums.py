# https://leetcode.com/problems/two-sum/

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         #for loop for the range of the nums []
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 #check to see if each num is equal to target
#                 if (nums[i] + nums[j]) == target and i != j:
#             #return the two index's where the two index's val equal that target
#                     return i, j
#         return None

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a dictionary from element in nums to index.
        elem_to_index = {}
        for i in range(len(nums)):
            # find the complement at each element in nums
            complement = target - nums[i]
            # if complement has been seen before, return index from dict, and i
            if complement in elem_to_index:
                return elem_to_index[complement], i
            # add nums[i] to the dictionary to mark it as seen
            elem_to_index[nums[i]] = i
        return None 