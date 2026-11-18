class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sol 1: Sum[0,n] - sum(num)
        # Tips: in Python: range(n) means 0 ~ n-1
        # total = sum(range(len(nums)+1))
        # num_sum = sum(nums)
        # return total - num_sum

        # Sol 2: hash set checking
        nums_set = set(nums)
        for i in range(len(nums)+1):
            if i not in nums_set:
                return i

            