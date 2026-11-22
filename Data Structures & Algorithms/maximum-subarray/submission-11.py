class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initial two arrays
        # -2 4 -1 2 -5
        
        best_after = [0]*len(nums)
        best_start_from = [0]*len(nums)
        
        best_start_from[-1]= best_after[-1]=nums[-1]

        for i in range(len(nums)-2, -1, -1):
            # Best start from: use pre_best start or new start
            best_start_from[i] = nums[i] + max(0, best_start_from[i+1])
            # Best_after: 
            best_after[i] = max(best_start_from[i],best_after[i+1] )
        return best_after[0]