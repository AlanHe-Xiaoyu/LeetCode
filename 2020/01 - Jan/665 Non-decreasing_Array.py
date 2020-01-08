class Solution:
    # nums: List[int]
    def checkPossibility(self, nums) -> bool:

        """
        Soln 1
        Runtime: 244 ms, faster than 5.79% of Python3 online submissions for Non-decreasing Array.
        Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Non-decreasing Array.
        """
        length = len(nums)
        changedIdx = -1
        for i in range(length - 1):
            before, after = nums[i], nums[i+1]
            if before > after:
                nums1, nums2 = nums[:], nums[:]
                nums1[i] = nums1[i+1]
                nums2[i+1] = nums2[i]
                changedIdx = i
                break
                
        if changedIdx == -1:
            return True
        
        flag1 = True
        for i in range(length - 1):
            before, after = nums1[i], nums1[i+1]
            if before > after:
                flag1 = False
                break
        if flag1:
            return True
        
        for i in range(length - 1):
            before, after = nums2[i], nums2[i+1]
            if before > after:
                return False
        return True