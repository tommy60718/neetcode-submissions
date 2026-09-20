class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. target = original or rotated?
        # 2. Find minimun
        # 3. Execute binary search in the targeted half

        # Initialize parameters
        l, r= 0, len(nums)-1
        m= (l+r)//2
        anchor = nums[0]        
        min_idx = 0

        # 1. flag: Original=False, Rotated=True
        if target >= anchor:
            flag = True
        else:
            flag = False
        
        # 2. Find minimum
        # Edge case checking: Fully rotated or only one element
        if nums[r] >= anchor:
            min_idx = 0
            l=r+1 # pass main checking
            flag = False
        # main algorithm
        while l< r:
            if nums[m] < anchor:
                r = m
            else:
                l = m+1
            m= (l+r)//2
        if l==r:
            min_idx = r

        # 3. Binary search
        # initialization
        if flag ==True:
            ls, rs = 0, min_idx-1
        else:
            ls, rs= min_idx, len(nums)-1
        ms = (ls+rs)//2
        
        while ls<=rs:
            if nums[ms] == target:
                return ms
            if nums[ms] > target:
                rs = ms-1
            else:
                ls = ms+1
            ms = (ls + rs)//2
        return -1




