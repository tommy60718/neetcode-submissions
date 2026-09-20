class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        
        # 1. Find Minimum (Template 2)
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # Compare to the rightmost element to cleanly find the pivot
            if nums[m] > nums[r]: 
                l = m + 1
            else:
                r = m
        
        min_idx = l
        
        # 2. Determine which half to search
        # If target is between the minimum and the very end, it's in the right half
        if min_idx <= len(nums) - 1 and target <= nums[-1]:
            l, r = min_idx, len(nums) - 1
        else: # Otherwise, it's in the left half
            l, r = 0, min_idx - 1
            
        # 3. Standard Binary Search (Template 1)
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return -1