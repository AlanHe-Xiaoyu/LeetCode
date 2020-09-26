class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """Max profit of +inf buy/sell(s)"""
        
        """
        Runtime: 60 ms, faster than 85.85% of Python3 online submissions for Best Time to Buy and Sell Stock II.
        Memory Usage: 15.1 MB, less than 57.64% of Python3 online submissions for Best Time to Buy and Sell Stock II.
        """
        curProf = 0
        curBuy = float('inf')
        for p in prices:
            if p > curBuy:
                curProf += (p - curBuy)
            curBuy = p

        return curProf