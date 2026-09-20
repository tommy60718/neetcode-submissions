class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exist_set = set(nums)
        max_seq =0

        for num in nums:
            single_max = 1
            if num-1 not in exist_set:
                seq_idx=num
                while seq_idx+1 in exist_set:
                    single_max+=1
                    seq_idx+=1
                max_seq = max(max_seq, single_max)


        return max_seq