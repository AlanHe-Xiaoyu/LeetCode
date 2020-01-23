class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        """
        Runtime: 52 ms, faster than 84.55% of Python3 online submissions for Combination Sum.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Combination Sum.
        """
        # Idea : go from smallest to largest
        length = len(candidates)
        candidates = sorted(candidates)
        def helper(idx, remainder, cur):
            nonlocal length
            if remainder == 0:
                return [cur]
            elif idx >= length or remainder < candidates[idx]:
                return [[]]
            
            first_item = candidates[idx]
            use_first = [lst for lst in helper(idx, remainder - first_item, cur + [first_item]) if lst != []]
            no_use_first = [lst for lst in helper(idx + 1, remainder, cur) if lst != []]
            
            return use_first + no_use_first
        
        result = helper(0, target, [])
        if result == [[]]:
            return []
        return result
