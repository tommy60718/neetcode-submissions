class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # -2 4 -1 2 -5
        l, r = 0, 0
        max_sum = nums[0]
        pre_max = nums[0]

        for i in range(1, len(nums), 1):
            if pre_max < 0 :
                pre_max = nums[i]
            else:
                pre_max += nums[i]
            max_sum = max(max_sum, pre_max)
        return max_sum