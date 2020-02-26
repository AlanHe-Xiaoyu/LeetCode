class Solution {
    public void reverseString(char[] s) {

        """
        Runtime: 1 ms, faster than 98.42% of Java online submissions for Reverse String.
        Memory Usage: 42.9 MB, less than 99.41% of Java online submissions for Reverse String.
        """
        for (int i = 0; i < s.length / 2; i++) {
            char temp = s[i];
            s[i] = s[s.length - i - 1];
            s[s.length - i - 1] = temp;
        }

        """
        Soln #2 (slight modification)
        Runtime: 1 ms, faster than 98.42% of Java online submissions for Reverse String.
        Memory Usage: 43.1 MB, less than 99.41% of Java online submissions for Reverse String.
        """
        for (int i = 0; i < (s.length-1) / 2.0; i++) {
            char temp = s[i];
            s[i] = s[s.length - i - 1];
            s[s.length - i - 1] = temp;
        }
    }
}