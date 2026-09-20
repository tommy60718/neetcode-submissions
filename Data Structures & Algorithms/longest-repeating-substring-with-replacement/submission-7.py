class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = defaultdict(int)
        max_sub =0
        l=0

        for r in range(len(s)):
            right_key = s[r]
            freq_dict[right_key]+=1
            highest_key = max(freq_dict, key=freq_dict.get)
            cumulative_value = 0
            for key, value in freq_dict.items():
                if key == highest_key:
                    continue
                cumulative_value += value
            if cumulative_value <= k:
                max_sub = max(max_sub, r-l +1)
            else:
                left_key = s[l]
                freq_dict[left_key] -=1
                l +=1
        return max_sub
        # AAABABB
        # BACBBAAAB, K=2
        # BAABB
        # Sliding window:
        # iterate r, update s[r] to freq_dict
        # See other keys' values exclude the key with highest value
        # If it <= k -> max_sub = max(max_sub, r-l+1)
        # If it > k -> freq_dict[l] -=1, l +=1

        


        