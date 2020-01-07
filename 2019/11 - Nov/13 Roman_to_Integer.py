class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Runtime: 40 ms, faster than 98.02% of Python3 online submissions for Roman to Integer.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
        """
        mapping = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        answerNum = mapping[s[0]]
        for i in range(1, len(s)):
            prevNum = mapping[s[i - 1]]
            curNum = mapping[s[i]]
            if prevNum >= curNum:
                answerNum += curNum
            else:
                answerNum += curNum - 2 * prevNum

        return answerNum
