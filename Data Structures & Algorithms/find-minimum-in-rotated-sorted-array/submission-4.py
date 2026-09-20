class Solution:
    def findMin(self, nums: List[int]) -> int:


        l, r= 0, len(nums)-1
        m = (l+r)//2
        anchor = nums[0]
        # fully rotated & only one element edge case checking
        if nums[r] >= anchor:
            return anchor

        # if m >= first element -> Rotated
        # if m < first element -> Original
        
        while l < r:
            if nums[m] >= anchor:
                l=m+1
            else:
                r =m
            if l==r:
                return nums[r]
            m = (l+r)//2


