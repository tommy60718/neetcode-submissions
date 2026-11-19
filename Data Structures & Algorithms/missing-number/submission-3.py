class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sol sum(0~n) - sum(nums)

        total = sum(range(len(nums)+1)) # 0 ~ n
        nums_sum = sum(nums) # n-1 elements
        return total - nums_sum