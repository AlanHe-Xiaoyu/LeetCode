class q516 {
    public static void main(String[] args) {
        String test = "abbbaaccaae"; // should be 6
        System.out.println(longestPalindromeSubseq(test));
    }

    public static int longestPalindromeSubseq(String s) {
        if (s.length() < 1) { return 0; }

        int max_len = -1;

        for (int i = 0; i < s.length(); i++) {
            int cur_len = expand_center(s, i);
            if (cur_len > max_len) {
                max_len = cur_len;
            }
        }

        return max_len;
    }

    public static int expand_center(String s, int idx) {
        int cur_max_odd = 1;
        int left = idx - 1;
        int right = idx + 1;

        while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
            cur_max_odd += 2;
            left--;
            right++;
        }

        int cur_max_even = 0;
        if (idx + 1 < s.length() && s.charAt(idx) == s.charAt(idx + 1)) {
            left = idx - 1;
            right = idx + 2;
            cur_max_even = 2;
        }

        while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
            cur_max_even += 2;
            left--;
            right++;
        }

        return Math.max(cur_max_odd, cur_max_even);
    }
}


// Below is the actual submission on LeetCode
/**
class Solution {
    public int longestPalindromeSubseq(String s) {
        if (s.length() < 1) { return 0; }

        int max_len = -1;

        for (int i = 0; i < s.length(); i++) {
            int cur_len = expand_center(s, i);
            if (cur_len > max_len) {
                max_len = cur_len;
            }
        }

        return max_len;
    }

    public int expand_center(String s, int idx) {
        int cur_max_odd = 1;
        int left = idx - 1;
        int right = idx + 1;

        while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
            cur_max_odd += 2;
            left--;
            right++;
        }

        int cur_max_even = 0;
        if (idx + 1 < s.length() && s.charAt(idx) == s.charAt(idx + 1)) {
            left = idx - 1;
            right = idx + 2;
            cur_max_even = 2;
        }

        while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
            cur_max_even += 2;
            left--;
            right++;
        }

        return Math.max(cur_max_odd, cur_max_even);
    }
}
*/
