class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        """
        Runtime: 28 ms, faster than 67.54% of Python3 online submissions for Jewels and Stones.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
        """
        count = 0
        for stone in S:
            if stone in J:
                count += 1
                
        return count