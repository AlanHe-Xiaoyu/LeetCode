class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
    
        """
        Runtime: 628 ms, faster than 99.90% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
        Memory Usage: 20.4 MB, less than 12.50% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
        """
        if prices == None or len(prices) < 2:
            return 0
        
        curPrice = float('inf')
        total = 0
        for p in prices:
            if p < curPrice:
                curPrice = p
            elif p > (curPrice + fee):
                total += (p - curPrice - fee)
                curPrice = p - fee
        return total