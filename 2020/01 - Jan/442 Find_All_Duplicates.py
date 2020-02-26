class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        """
        Runtime: 400 ms, faster than 47.79% of Python3 online submissions for Find All Duplicates in an Array.
        Memory Usage: 20.3 MB, less than 35.71% of Python3 online submissions for Find All Duplicates in an Array.
        """
        result = []
        for i in range(len(nums)):
            cur = nums[i]
            if nums[abs(cur) - 1] < 0:
                result.append(abs(cur))
            else:
                nums[abs(cur) - 1] = -nums[abs(cur) - 1]
            
        return result