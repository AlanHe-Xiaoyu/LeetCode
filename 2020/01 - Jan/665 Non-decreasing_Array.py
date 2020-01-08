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

        """
        Runtime: 204 ms, faster than 45.68% of Python3 online submissions for Non-decreasing Array.
        Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Non-decreasing Array.
        """
        length = len(nums)
        problemIdx = -1
        for i in range(length - 1):
            before, after = nums[i], nums[i+1]
            if before > after:
                if problemIdx == -1:
                    problemIdx = i
                else:
                    return False
        
        if problemIdx == -1:
            return True
        
        # Special unique case
        if problemIdx == 0 or problemIdx == length - 2:
            return True
        else:
            # x; problem; problem+1; x
            lst = nums[problemIdx - 1 : problemIdx + 3]
            return lst[0] <= lst[2] or lst[1] <= lst[3]

        """
        Runtime: 188 ms, faster than 97.77% of Python3 online submissions for Non-decreasing Array.
        Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Non-decreasing Array.
        """
        length = len(nums)
        changed = False
        for i in range(length - 1):
            before, after = nums[i], nums[i+1]
            if before > after:
                if changed:
                    return False
                if i >= 1 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                changed = True
        return True