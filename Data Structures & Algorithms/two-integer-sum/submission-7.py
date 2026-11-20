class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traversed = {} # key:value = num:idx
        # 5,3,6,4 -> 7
        for i, num in enumerate(nums):
            if target-num not in traversed:
                traversed[num] = i
            else:
                return [traversed[target-num], i]