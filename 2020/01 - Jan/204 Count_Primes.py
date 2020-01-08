class Solution:
    def countPrimes(self, n: int) -> int:
        
        """
        Runtime: 856 ms, faster than 31.74% of Python3 online submissions for Count Primes.
        Memory Usage: 24.2 MB, less than 100.00% of Python3 online submissions for Count Primes.
        """
        if n <= 2:
            return 0
        
        isPrime = [True] * n
        
        for i in range(2, n):
            if isPrime[i]:
                for j in range(2, (n-1) // i + 1):
                    isPrime[i * j] = False
        
        # ignore 0 and 1
        return sum(isPrime) - 2