# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         #create a set with the numbers from the list
#         nums_set = set(nums)    
#         #return len of numbers if not equal to number in set
#         return len(nums) != len(nums_set)  

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a set to store nums in array that we have seen before
        nums_set = set()  
        #iterate through nums list
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
