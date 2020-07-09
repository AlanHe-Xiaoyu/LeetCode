class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        """
        Runtime: 236 ms, faster than 80.60% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
        Memory Usage: 17.2 MB, less than 21.01% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
        """
        seen = [0] * 60
        count = 0
        for t in time:
            count += seen[(-t) % 60]
            seen[t % 60] += 1
        return count