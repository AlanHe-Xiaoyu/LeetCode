class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        Runtime: 36 ms, faster than 39.96% of Python3 online submissions for Generate Parentheses.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Generate Parentheses.
        """
        answer = []
        def helper(cur, left, right):
            nonlocal answer
            if len(cur) == 2 * n:
                answer.append(cur)
                return
            if left < n:
                helper(cur + '(', left + 1, right)
            if right < left:
                helper(cur + ')', left, right + 1)
            
        helper("", 0, 0)
        return answer