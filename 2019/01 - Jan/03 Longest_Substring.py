class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Soln 1 - Brute Force, O(n^2)
        # @time = 1036 ms
        maxLen = 0
        curLen = 0
        occurred = {}

        for i in range(len(s)):
            curLen = 1
            occurred = {s[i]: 1}
            for j in range(i+1, len(s)):
                letter = s[j]
                if (occurred.get(letter, 0) != 0):
                    break
                else:
                    occurred[letter] = 1
                    curLen += 1
            maxLen = max(maxLen, curLen)
                    
        return maxLen



        # Soln 2
        # @time
        