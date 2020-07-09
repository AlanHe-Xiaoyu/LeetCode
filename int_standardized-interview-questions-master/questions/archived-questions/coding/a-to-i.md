# A to I
- Maintainer: @yotam.mosinzon

## Overview

This question asks the candidate to implement an algorithm parsing a string and extracting an integer from it. The idea comes from the C function atoi().

## Prompts

This problem is presented as a single prompt, given in a format that might appear in a work ticket:

```
/*
    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
    Example 1:

    Input: "42"
    Output: 42
    Example 2:

    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                Then take as many numerical digits as possible, which gets 42.
    Example 3:

    Input: "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
    Example 4:

    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical 
                digit or a +/- sign. Therefore no valid conversion could be performed.
    Example 5:

    Input: "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                Thefore INT_MIN (−231) is returned.
*/
```

This is normally copy/pasted directly into an editor, and the candidate should be asked to read through the question and encouraged to ask any questions they might have.

----

#### Expected questions from the candidate

- Input Types: a String.

- Running Time: try to get a working solution, then optimize.

#### What do we want to see/hear?

- We want to candidate to describe additional possible test cases, split the code into relevant functions, isolating the edge cases to be handled correctly.

## Example Solutions

- [Java](#java)

# Java

```Java
class Solution {
    public int myAtoi(String str) {
        int i = 0;
        while (i < str.length() && (str.charAt(i) == ' ')) i++;
        
        if (i < str.length()) {
            char first = str.charAt(i);
            if (first >= '0' && first <= '9') {
                int j = i;
                while (i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9') i++;
                
                return handleParsing(str.substring(j, i));
            } else if ((first == '-' || first == '+') && i < str.length( -1 && str.charAt(i + 1) <= '9' && str.charAt(i + 1) >= '0') {
                int j = i++;
                while (i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9') i++;
                
                return handleParsing(str.substring(j, i));
            }
        }
        
        return 0;
    }
    private int handleParsing(String str) {
        if (str.length() < 1) return 0;
        int j = 0;
        while (j < str.length() && str.charAt(j) == '0') j++;
        
        if (j == str.length()) return 0;
        
        str = str.substring(j, str.length());
        
        if (str.charAt(0) == '-' || str.charAt(0) == '+') {
            int i = 1;
            while (i < str.length() && str.charAt(i) == '0') i++;
            
            str = str.substring(0, 1) + "0" + str.substring(i, str.length());
        }
        
        if (str.charAt(0) == '-') {
            if (str.length() > 14) return Integer.MIN_VALUE;
            long temp = Long.parseLong(str);
            
            if (temp < Integer.MIN_VALUE) return Integer.MIN_VALUE;
            return (int) temp;
        }
        
        if (str.length() > 13) return Integer.MAX_VALUE;
        long temp = Long.parseLong(str);
        
        if (temp > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        return (int) temp;
    }
}
```
