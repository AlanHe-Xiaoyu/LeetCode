class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
        Soln #1
        Runtime: 244 ms, faster than 8.68% of Python3 online submissions for Permutation in String.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Permutation in String.
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        s1_len = len(s1)
        if s1_len > len(s2):
            return False
        
        s1_hash = 1
        for letter in s1:
            s1_hash *= primes[ord(letter) - ord('a')]
        
        s2_cur_hash = 1
        for i in range(s1_len):
            s2_cur_hash *= primes[ord(s2[i]) - ord('a')]
        
        if s1_hash == s2_cur_hash:
            return True
        
        for i in range(s1_len, len(s2)):
            prev_prime, cur_prime = primes[ord(s2[i - s1_len]) - ord('a')], primes[ord(s2[i]) - ord('a')]
            s2_cur_hash = s2_cur_hash * cur_prime // prev_prime
            if s1_hash == s2_cur_hash:
                return True
        
        return False

        """
        Soln #2
        Runtime: 72 ms, faster than 53.26% of Python3 online submissions for Permutation in String.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Permutation in String.
        """
        def compare_dicts(d1, d2):
            for (k, v) in d1.items():
                if k not in d2.keys() or d2[k] != v:
                    return False
            return True

        cnt1, cnt2 = {}, {}
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False

        for i in range(s1_len):
            l1, l2 = s1[i], s2[i]
            cnt1[l1] = cnt1.get(l1, 0) + 1
            cnt2[l2] = cnt2.get(l2, 0) + 1
        
        for i in range(s1_len, s2_len):
            if compare_dicts(cnt1, cnt2):
                return True
            prev_letter, new_letter = s2[i - s1_len], s2[i]
            cnt2[prev_letter] -= 1
            cnt2[new_letter] = cnt2.get(new_letter, 0) + 1
        
        return compare_dicts(cnt1, cnt2)
