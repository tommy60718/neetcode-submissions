class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # when r finding a lower buy point, l become it, and this become 
        # the new dominate point
        
        # 10 1 5 6 7 1
        l, r= 0, 1
        max_profit = 0
        while r < len(prices):
            max_profit = max(max_profit, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return max_profit