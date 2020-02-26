class Solution {
    public int singleNumber(int[] nums) {

        """
        Soln #1 - O(n) time and space
        Runtime: 4 ms, faster than 43.68% of Java online submissions for Single Number.
        Memory Usage: 41.7 MB, less than 57.04% of Java online submissions for Single Number.
        """
        HashSet<Integer> single = new HashSet<>();
        int total = 0;
        for (int n : nums) {
            single.add(n);
            total += n;
        }
        
        int singleTotal = 0;
        for (int n : single) {
            singleTotal += n;
        }
        
        return singleTotal * 2 - total;

        """
        Soln #2 - O(1) space with Bit Manipulation
        Runtime: 0 ms, faster than 100.00% of Java online submissions for Single Number.
        Memory Usage: 42.1 MB, less than 5.93% of Java online submissions for Single Number.
        """
        int answer = 0;
        for (int n : nums) {
            answer ^= n;
        }
        return answer;
    }
}