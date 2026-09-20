class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] +=1

        sorted_keys = sorted ( freq_map.keys(), key=lambda x: freq_map[x], reverse = True )

        return sorted_keys[:k]