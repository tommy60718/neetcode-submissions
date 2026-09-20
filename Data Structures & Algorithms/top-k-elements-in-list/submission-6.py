from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Using defaultdict(int) initializes any new key with a default value of 0
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        # This cleanly replaces the old .get() syntax
        for num in nums:
            count[num] += 1
            
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res