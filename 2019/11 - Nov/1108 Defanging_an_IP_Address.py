class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Runtime: 20 ms, faster than 99.52% of Python3 online submissions for Defanging an IP Address.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
        """
        outputAddress = ""
        for letter in address:
            if letter == '.':
                outputAddress += '[.]'
            else:
                outputAddress += letter
                
        return outputAddress


        """
        Soln 2 - lol
        Runtime: 20 ms, faster than 99.52% of Python3 online submissions for Defanging an IP Address.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
        """
        return address.replace('.', '[.]')