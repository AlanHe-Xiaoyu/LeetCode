class Solution:
    def reverse(self, x: int) -> int:
        """
        Runtime: 28 ms, faster than 97.31% of Python3 online submissions for Reverse Integer.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
        """
        answer = 0
        sign = (x >= 0)
        x = abs(x)
        while x > 0:
            digit, x = x % 10, x // 10
            answer = answer * 10 + digit
        answer = answer * (sign * 2 - 1)
        if answer < -pow(2, 31) or answer >= pow(2, 31):
            return 0
        return answer

