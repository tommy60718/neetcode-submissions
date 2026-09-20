class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # z x x y z y x
        l = 0
        max_sub = 0
        cur_sub = set()
        
        for r in range(len(s)):
            while s[r] in cur_sub:
                cur_sub.remove(s[l])
                l+=1
            max_sub = max(max_sub, r - l + 1)
            cur_sub.add(s[r])
        return max_sub

            
