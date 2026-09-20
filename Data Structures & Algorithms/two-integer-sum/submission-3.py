class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        dif = 0
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hashmap:
                return [hashmap[dif], i]
            hashmap[nums[i]]=i
