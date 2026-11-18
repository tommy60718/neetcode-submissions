class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sol 1: Sum[0,n] - sum(num)
        # extract nums by all the elements in 0~n-1
        # Tips: in Python: range(n) means 0 ~ n-1
        total = sum(range(len(nums)+1))
        num_sum = sum(nums)
        return total - num_sum
            