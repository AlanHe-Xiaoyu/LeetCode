class Solution {
    public String longestCommonPrefix(String[] strs) {

        """
        Runtime: 0 ms, faster than 100.00% of Java online submissions for Longest Common Prefix.
        Memory Usage: 37.6 MB, less than 84.80% of Java online submissions for Longest Common Prefix.
        """
        if (strs == null || strs.length == 0) {
            return "";
        }
        
        String firstStr = strs[0];
        for (int i = 0; i < firstStr.length(); i++) {
            char curChar = firstStr.charAt(i);
            for (int strIdx = 1; strIdx < strs.length; strIdx++) {
                if (i == strs[strIdx].length() || curChar != strs[strIdx].charAt(i)) {
                    return firstStr.substring(0, i);
                }
            }
        }
        return firstStr;
    }
}