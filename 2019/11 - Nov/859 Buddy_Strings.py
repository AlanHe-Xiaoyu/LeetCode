class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        """
        Runtime: 32 ms, faster than 95.03% of Python3 online submissions for Buddy Strings.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Buddy Strings.
        """
        lenA = len(A)
        if lenA != len(B):
            return False
        count = 0
        difIdx = []
        allLetters = set()
        hasDouble = False
        for i in range(lenA):
            A_i = A[i]
            if not hasDouble:
                if A_i in allLetters:
                    hasDouble = True
                else:
                    allLetters.add(A_i)

            if A_i != B[i]:
                count += 1
                difIdx.append(i)
            if count > 2:
                return False

        if count == 0:
            return hasDouble
        elif count == 1:
            return False
        else: # count == 2
            idx1, idx2 = difIdx[0], difIdx[1]
            return A[idx1] == B[idx2] and A[idx2] == B[idx1]
        