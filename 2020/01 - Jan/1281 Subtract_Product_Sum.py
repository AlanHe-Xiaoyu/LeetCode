class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        """
        Runtime: 20 ms, faster than 95.94% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
        """
        if n == 0:
            return 0
        
        digit_prod, digit_sum = 1, 0
        while n > 0:
            digit, n = n % 10, n // 10
            digit_prod *= digit
            digit_sum += digit
        return digit_prod - digit_sum