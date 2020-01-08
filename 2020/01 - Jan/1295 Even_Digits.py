class Solution:
    # nums: List[int]
    def findNumbers(self, nums) -> int:

        """
        Runtime: 52 ms, faster than 72.99% of Python3 online submissions for Find Numbers with Even Number of Digits.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
        """
        
        count = 0
        for n in nums:
            if (10 <= n <= 99) or (1000 <= n <= 9999):
                count += 1
        return count