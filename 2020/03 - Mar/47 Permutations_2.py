class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        """
        Runtime: 52 ms, faster than 82.48% of Python3 online submissions for Permutations II.
        Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Permutations II.
        """
        ans = [nums]
        for i in range(1, len(nums)):
            length = len(ans)
            for k in range(length):
                for j in range(i - 1, -1, -1):
                    if ans[k][i] == ans[k][j]: # if same then no copy
                        break
                    ans.append(ans[k].copy())
                    ans[-1][i], ans[-1][j] = ans[-1][j], ans[-1][i]

        return ans