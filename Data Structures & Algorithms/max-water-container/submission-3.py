class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r= 0, len(heights)-1
        max_volume =0
        while l < r:
            this_volume = 0
            this_volume= min(heights[l], heights[r]) * (r-l)
            max_volume = max(this_volume, max_volume)
            if heights[l]> heights[r]:
                r -=1
            else:
                l+=1
        return max_volume