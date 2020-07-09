class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        """
        Runtime: 96 ms, faster than 92.73% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
        Memory Usage: 14.2 MB, less than 66.67% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
        """
        if k > (len(prices) / 2):
            return sum([prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i-1]])
            
        buys = [-float('inf')] * (k+1) # After each buy
        sells = [0] * (k+1) # After each sell
        for p in prices:
            for i in range(1, k+1):
                buys[i] = max(buys[i], sells[i-1] - p)
                sells[i] = max(sells[i], buys[i] + p) # Sell today
            
        return sells[k]