import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        """
        Runtime: 32 ms, faster than 70.24% of Python3 online submissions for Most Common Word.
        
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Most Common Word.
        """
        paragraph = paragraph.lower()
        for w in "!?,.';:":
            paragraph = paragraph.replace(w, " ")
        
        lst_words = paragraph.strip().split(" ")

        count = {}
        for word in lst_words:
            count[word] = count.get(word, 0) + 1

        for ban in set(banned):
            count[ban] = 0
        count[" "] = 0
        count[""] = 0
            
        return max(count, default=None, key=lambda k : count[k])
        


        """
        Soln #2 - use a Counter()
        Runtime: 28 ms, faster than 89.60% of Python3 online submissions for Most Common Word.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Most Common Word.
        """
        paragraph = paragraph.lower()
        for w in "!?,.';:":
            paragraph = paragraph.replace(w, " ")
        
        lst_words = paragraph.strip().split(" ")

        count = collections.Counter(lst_words)

        for ban in set(banned):
            count[ban] = 0
        count[" "] = 0
        count[""] = 0
            
        return max(count, default=None, key=lambda k : count[k])