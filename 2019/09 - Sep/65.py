'''
Validate if a given string can be interpreted as a decimal number.
'''

class Solution:
    def isNumber(self, s: str) -> bool:        
        try:
            float(s)
            return True
        except:
            return False