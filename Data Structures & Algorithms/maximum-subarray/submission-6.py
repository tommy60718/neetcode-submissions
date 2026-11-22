class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Two pointer
        # -1, 2, 1, -5, 4
        l, r = 0, 1
        max_sum = nums[0]
        pre_max = nums[0]
        for i in range(1, len(nums),1):
            if pre_max <0:
                pre_max = nums[i]
            else:
                pre_max += nums[i]
            max_sum = max(max_sum, pre_max)
        return max_sum
        
        # -1, 2, 1, -5, 4
        # start_at = [0] * len(nums)
        # best_from = [0] * len(nums)

        # # initialize the last
        # best_from[-1] = start_at[-1] = nums[-1]
        # for i in range(len(nums)-2, -1, -1):
        #     # start_at: choose eliminate the rest or continue
        #     start_at[i] = nums[i] + max(0, start_at[i+1])
        #     # best_from: choose to include current num or not
        #     best_from[i] = max(best_from[i+1], start_at[i])
        # return best_from[0]

        
            
