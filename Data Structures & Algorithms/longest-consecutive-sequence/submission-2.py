class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        appear_map = defaultdict(bool)
        max_seq =0

        for num in nums:
            appear_map[num]=True
        
        next = False
        for num in nums:
            single_seq =1
            seq_num=num+1
            while appear_map[seq_num]==True:
                single_seq+=1
                seq_num +=1
            max_seq = max(single_seq, max_seq)
        return max_seq