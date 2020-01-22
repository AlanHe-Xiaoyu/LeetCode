class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:

        """
        Runtime: 168 ms, faster than 58.33% of Python3 online submissions for Consecutive Numbers Sum.
        Memory Usage: 12.4 MB, less than 100.00% of Python3 online submissions for Consecutive Numbers Sum.
        """
        import math
        cnt = 1
        for i in range(2, int(math.sqrt(N * 2)) + 1):
            if (i % 2 == 1) and (N % i == 0): # odd
                mid = N // i
                min_num = mid - (N // i - 1) // 2
                if min_num >= 1:
                    cnt += 1
            elif (i % 2 == 0): # even
                num_pairs = i // 2
                if N % num_pairs == 0:
                    pair_sum = N // num_pairs
                    if pair_sum % 2 == 1: # must be odd
                        mid_big = (pair_sum + 1) // 2
                        min_num = mid_big - num_pairs
                        if min_num >= 1:
                            cnt += 1
                        
        return cnt
