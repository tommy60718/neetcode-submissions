class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # -2 4 -1 2 -5
        best_start = [0] * len(nums)
        best_after = [0] * len(nums)
        best_after[-1] = best_start[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            best_start[i] = nums[i] + max(0, best_start[i+1])
            best_after[i] = max ( best_start[i], best_after[i+1])
        return best_after[0]



        # -2 4 -1 2 -5
        # max_sum = nums[0]
        # pre_max = nums[0]

        # for i in range(1, len(nums), 1):
        #     if pre_max < 0 :
        #         pre_max = nums[i]
        #     else:
        #         pre_max += nums[i]
        #     max_sum = max(max_sum, pre_max)
        # return max_sum