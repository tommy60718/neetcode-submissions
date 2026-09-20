from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Automatically sets new keys to 0
        countS, countT = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1  # This works perfectly now!
            countT[t[i]] += 1
        
        for c in countS:
            if countS[c] != countT[c]:
                return False
        return True