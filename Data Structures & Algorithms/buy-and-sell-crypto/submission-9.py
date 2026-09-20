class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # when r finding a lower buy point, l become it, and this become 
        # the new dominate point
        
        # 10 1 5 6 7 1
        # l, r= 0, 1
        # max_profit = 0
        # while r < len(prices):
        #     max_profit = max(max_profit, prices[r]-prices[l])
        #     if prices[r] < prices[l]:
        #         l = r
        #     r += 1
        # return max_profit

        l=0
        max_profit = 0
        
        for r in range(len(prices)):
            if prices[r]<prices[l]:
                l=r
            max_profit = max(max_profit, prices[r]-prices[l])
        return max_profit
