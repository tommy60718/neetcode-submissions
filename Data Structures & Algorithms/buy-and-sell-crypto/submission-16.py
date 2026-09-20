class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10, 2, 6, 5, 7, 1, 11(len-1)

        l, r=0, 1
        max_profit = 0
        global_min = 101

        # two-pointer main loop
        # check boundary to enter while loop
        while l<= (len(prices)-1) and r <= (len(prices)-1):
            # Check global minimum, update l if needed
            if prices[r] < prices[l]:
                l = r
                r +=1
                continue
            # l & r both eligible, check max
            max_profit = max(prices[r] - prices[l], max_profit)
            # finished check, update r, prepare for next itr
            r += 1 
        return max_profit

        
