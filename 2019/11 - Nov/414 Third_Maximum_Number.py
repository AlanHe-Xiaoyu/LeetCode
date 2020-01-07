class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Given non-empty

        """
        Soln 1
        Runtime: 64 ms, faster than 58.82% of Python3 online submissions for Third Maximum Number.
        Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Third Maximum Number.
        """

        max3 = []
        for n in nums:
            if n in max3:
                continue
            if len(max3) < 3:
                max3.append(n)
            else:
                max3 = sorted(max3)
                if n > max3[0]:
                    max3[0] = n
            print(max3)

        if len(max3) < 3:
            return max(max3)
        else:
            return min(max3)



        """
        Soln 2
        Runtime: 64 ms, faster than 58.82% of Python3 online submissions for Third Maximum Number.
        Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Third Maximum Number.
        """
        max3 = [-float('inf'), -float('inf'), -float('inf')]
        for n in nums:
            if n > max3[2]:
                max3 = [max3[1], max3[2], n]
            elif n > max3[1] and n < max3[2]:
                max3 = [max3[1], n, max3[2]]
            elif n > max3[0] and n < max3[1]:
                max3[0] = n

        if max3[0] == -float('inf'):
            return max3[2]
        else:
            return max3[0]