class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        Soln #1
        Runtime: 2336 ms, faster than 6.50% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 13.8 MB, less than 96.55% of Python3 online submissions for Best Time to Buy and Sell Stock.
        """
        max_diff = 0
        cur_min, cur_max = float('inf'), float('inf')
        for i in range(len(prices) - 1):
            cur = prices[i]
            if cur < cur_min and cur < cur_max:
                max_sell = max(prices[i+1:])
                max_diff = max(max_diff, max_sell - cur)
                cur_min, cur_max = cur, max_sell
                
        return max_diff
        

        """
        Soln #2
        Runtime: 96 ms, faster than 6.50% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 13.7 MB, less than 98.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
        """
        if len(prices) == 0:
            return 0
        
        cur_min, max_diff = prices[0], 0
        for num in prices[1:]:
            if num < cur_min:
                cur_min = num
            else:
                max_diff = max(max_diff, num - cur_min)
                
        return max_diff


        """
        Soln #3 (mutation of #2)
        Runtime: 60 ms, faster than 81.69% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock.
        """
        cur_min, max_diff = float('inf'), 0
        for num in prices:
            if num < cur_min:
                cur_min = num
            else:
                cur_diff = num - cur_min
                if max_diff < cur_diff:
                    max_diff = cur_diff
                
        return max_diff


        """
        Soln #4 - slight adjustment (speedup due to less max/min op's)
        Runtime: 56 ms, faster than 94.43% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 15.1 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
        """
        curMin = float('inf')
        maxProf = 0
        for p in prices:
            if p < curMin:
                curMin = p
            elif p > (maxProf + curMin):
                maxProf = p - curMin
                
        return maxProf