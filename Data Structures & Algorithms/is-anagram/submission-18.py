
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False
        
        freqS, freqT = defaultdict(int), defaultdict(int)

        for c in s:
            freqS[c] += 1
        for c in t:
            freqT[c] += 1 
        for key in freqS:
            if freqS[key] != freqT[key]:
                return False
        return True