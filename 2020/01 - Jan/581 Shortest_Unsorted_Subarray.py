class Solution:
    # nums: List[int]
    def findUnsortedSubarray(self, nums) -> int:

        """
        Soln 1 - basic idea : sorting -> O(n log n) time
        Runtime: 224 ms, faster than 50.00% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
        Memory Usage: 14 MB, less than 85.00% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
        """
        sorted_nums = sorted(nums[:])
        startingIdx = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                startingIdx = i
                break
        
        if startingIdx == -1:
            return 0
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != sorted_nums[i]:
                endingIdx = i
                break
        
        return endingIdx - startingIdx + 1