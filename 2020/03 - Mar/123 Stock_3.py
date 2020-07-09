class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        Runtime: 76 ms, faster than 79.49% of Python3 online submissions for Best Time to Buy and Sell Stock III.
        Memory Usage: 14.9 MB, less than 54.55% of Python3 online submissions for Best Time to Buy and Sell Stock III.
        """
        length = len(prices)
        if not prices or length < 2:
            return 0
#         Including self, the min of prices[1:i+1]
        leftMins = [prices[0]] * length
        for i in range(1, length):
            if prices[i] < leftMins[i-1]:
                leftMins[i] = prices[i]
            else:
                leftMins[i] = leftMins[i-1]
                
#         Start ~DP, sold on current day and does Q121 for later
        maxPro = 0
        maxSecondPro = 0
        maxSell = -float('inf')
        for i in range(length-1, -1, -1):
            maxSell = max(maxSell, prices[i])
            maxSecondPro = max(maxSecondPro, maxSell - prices[i])
            firstPro = prices[i] - leftMins[i]
            maxPro = max(maxPro, firstPro + maxSecondPro)
            
        return maxPro


        """
        Runtime: 84 ms, faster than 48.71% of Python3 online submissions for Best Time to Buy and Sell Stock III.
        Memory Usage: 15.1 MB, less than 54.55% of Python3 online submissions for Best Time to Buy and Sell Stock III.
        """
        buys = [-float('inf'), -float('inf')] # After 1 buy, after 2 buys
        sells = [0, 0] # After 1 sell, after 2 sells
        for p in prices:
            buys[0] = max(buys[0], -p)
            sells[0] = max(sells[0], buys[0] + p) # Sell today
            buys[1] = max(buys[1], sells[0] - p)
            sells[1] = max(sells[1], buys[1] + p)
            
        return sells[1]