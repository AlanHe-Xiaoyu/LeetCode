class Solution:
    def convertToTitle(self, n: int) -> str:

        """
        Soln 1
        Runtime: 28 ms, faster than 94.59% of Python3 online submissions for Excel Sheet Column Title.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Title.
        """
        answer = ""
        while n > 0:
            letterAscii, n = (n - 1) % 26, (n - 1) // 26
            answer = chr(letterAscii + 65) + answer
        return answer



        """
        Soln 2 (same)
        Runtime: 28 ms, faster than 94.59% of Python3 online submissions for Excel Sheet Column Title.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Title.
        """
        answer = ""
        while n > 0:
            n -= 1
            letterAscii, n = n % 26, n // 26
            answer = chr(letterAscii + 65) + answer
        return answer