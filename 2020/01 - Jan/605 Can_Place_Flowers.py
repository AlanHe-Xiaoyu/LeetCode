class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        """
        Runtime: 232 ms, faster than 5.61% of Python3 online submissions for Can Place Flowers.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Can Place Flowers.
        """
        if len(flowerbed) == 0:
            return True # since n always <= size
        if len(flowerbed) == 1:
            return n == 0 or flowerbed[0] == 0
        
        flowers_added = 0
        if flowerbed[0] + flowerbed[1] == 0:
            flowerbed[0] = 1
            flowers_added += 1
        if flowerbed[-1] + flowerbed[-2] == 0:
            flowerbed[-1] = 1
            flowers_added += 1
            
        i = 1
        while i < len(flowerbed) - 1:
            if flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] == 0:
                flowerbed[i] = 1
                flowers_added += 1
                i += 2
            else:
                i += 1
                
        return flowers_added >= n
