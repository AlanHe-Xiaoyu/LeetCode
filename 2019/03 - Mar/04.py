class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # Soln 1 - Brute Force, O(m+n)
        # @time = 100 ms
        # @memory = 13.3 MB
        total = []
        idx1, idx2 = 0, 0
        len1, len2 = len(nums1), len(nums2)

        if len1 == 0:
            total = nums2
        elif len2 == 0:
            total = nums1
        else:
            while idx1 < len1 and idx2 < len2:
                if (nums1[idx1]) <= (nums2[idx2]):
                    total.append(nums1[idx1])
                    idx1 += 1
                else:
                    total.append(nums2[idx2])
                    idx2 += 1

            if (idx1 == len1):
                total.extend(nums2[idx2:])
            else:
                total.extend(nums1[idx1:])

        if (len1 + len2) % 2 == 0:
            return (total[(len1 + len2) // 2 - 1] + total[(len1 + len2) // 2]) / 2
        else:
            return total[(len1 + len2) // 2] / 1


        print('Soln 2')
        # Soln 2 - Brute Force + In Place, O(m+n)
        # @time
        # @memory
        def medianOddEven(lst, len):
            if len % 2 == 1:
                return lst[len // 2]
            else:
                return (lst[len // 2 - 1] + lst[len // 2]) / 2

        len1, len2 = len(nums1), len(nums2)

        if len1 == 0:
            return medianOddEven(nums2, len2)
        elif len2 == 0:
            return medianOddEven(nums1, len1)
        

        

a = Solution()        
print(a.findMedianSortedArrays([1], [1]))
print(a.findMedianSortedArrays([], [1]))
print(a.findMedianSortedArrays([3,4,5], [1]))