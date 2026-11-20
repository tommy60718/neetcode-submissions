class Solution:
    def climbStairs(self, n: int) -> int:
        # Buttom-up DP

        one, two = 1, 1

        for i in range(n-1): # We have 0, 1, ... , 5, len(stairs)=n+1=6
            tmp = one
            one = one + two
            two = tmp
        return one