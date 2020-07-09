class Solution:
    def isValid(self, s: str) -> bool:

        """
        Runtime: 28 ms, faster than 81.56% of Python3 online submissions for Valid Parentheses.
        Memory Usage: 13.9 MB, less than 50.41% of Python3 online submissions for Valid Parentheses.
        """
        stack = []
        opens = ["(", "{", "["]
        # closes = [")", "}", "]"]
        
        for e in s:
            if e in opens:
                stack.append(e)
            else:
                if len(stack) == 0:
                    return False
                
                cur_open = stack.pop()

                # Can also compare idx, but slow
                # open_idx = opens.index(cur_open)
                # close_idx = closes.index(e)

                if not ((cur_open == "(" and e == ")") or (cur_open == "{" and e == "}") or (cur_open == "[" and e == "]")):
                    return False
                
        return len(stack) == 0