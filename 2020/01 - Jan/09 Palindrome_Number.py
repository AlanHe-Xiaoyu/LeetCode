class Solution:
    def isPalindrome(self, x: int) -> bool:

        """
        Soln 1
        Runtime: 68 ms, faster than 38.50% of Python3 online submissions for Palindrome Number.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
        """
        if x < 0:
            return False
        
        reverse = 0
        x_copy = x
        while x_copy > 0:
            digit, x_copy = x_copy % 10, x_copy // 10
            reverse = reverse * 10 + digit
        
        return (reverse == x)


        """
        Soln 2
        Runtime: 52 ms, faster than 86.34% of Python3 online submissions for Palindrome Number.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
        """
        x_str = str(x)
        reversed_str = ''.join(reversed(x_str))
        return x_str == reversed_str
        
        
        """
        Soln 3
        Runtime: 36 ms, faster than 99.70% of Python3 online submissions for Palindrome Number.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
        """
        return str(x) == str(x)[::-1]