class Solution:
    def titleToNumber(self, s: str) -> int:

        """
        Runtime: 28 ms, faster than 97.10% of Python3 online submissions for Excel Sheet Column Number.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.
        """
        answer = 0
        for letter in s:
            answer = answer * 26 + (ord(letter) - 64)
        return answer