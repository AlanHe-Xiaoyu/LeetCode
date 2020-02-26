class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        """
        Runtime: 76 ms, faster than 82.45% of Python3 online submissions for Group the People Given the Group Size They Belong To.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Group the People Given the Group Size They Belong To.
        """
        grouped = {}
        for idx, size in enumerate(groupSizes):
            if size in grouped:
                grouped[size].append(idx)
            else:
                grouped[size] = [idx]
                
        result = []
        for size, curGroup in grouped.items():
            result.extend([curGroup[k*size : (k+1)*size] for k in range(len(curGroup) // size)])
            
        return result

        