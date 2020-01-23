class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        """
        Soln #1
        Runtime: 1788 ms, faster than 5.02% of Python3 online submissions for K-diff Pairs in an Array.
        Memory Usage: 14.3 MB, less than 96.77% of Python3 online submissions for K-diff Pairs in an Array.
        """
        if k == 0:
            count = 0
            d = {}
            for n in nums:
                if n not in d.keys():
                    d[n] = 1
                elif d[n] == 1:
                    count += 1
                    d[n] = 2
            return count
        elif k < 0: # lol wtf
            return 0
            
        cleaned = list(set(nums))
        count = 0
        for n in cleaned:
            if n+k in cleaned:
                count += 1
                
        return count

        """
        Soln #2
        Runtime: 236 ms, faster than 11.15% of Python3 online submissions for K-diff Pairs in an Array.
        Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for K-diff Pairs in an Array.
        """
        if k < 0:
            return 0
        
        from collections import Counter
        cleaned = Counter(nums)
        if k == 0:
            return len([v for v in cleaned.values() if v >= 2])
        
        cnt = 0
        for n in cleaned.keys():
            if n+k in cleaned:
                cnt += 1
                
        return cnt