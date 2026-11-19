class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sol 1: sum(0~n) - sum(nums)

        # total = sum(range(len(nums)+1)) # 0 ~ n
        # nums_sum = sum(nums) # n-1 elements
        # return total - nums_sum

        # Sol 2: 
        nums_set = set(nums)
        for i in range(len(nums)+1): # looping from 0 ~ n
            if i not in nums_set:
                return i