class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {

        """
        Runtime: 5 ms, faster than 82.47% of Java online submissions for Find All Numbers Disappeared in an Array.
        Memory Usage: 48.2 MB, less than 37.74% of Java online submissions for Find All Numbers Disappeared in an Array.
        """
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int cur = Math.abs(nums[i]) - 1;
            if (nums[cur] > 0) { nums[cur] = - nums[cur]; }
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) { result.add(i + 1); }
        }

        """
        Soln 2 : less comparison; might overflow
        Runtime: 5 ms, faster than 82.47% of Java online submissions for Find All Numbers Disappeared in an Array.
        Memory Usage: 48.2 MB, less than 37.74% of Java online submissions for Find All Numbers Disappeared in an Array.
        """
        List<Integer> result = new ArrayList<>();
        int len = nums.length;
        for (int i = 0; i < len; i++) {
            nums[(nums[i] - 1) % len] += len;
        }
        for (int i = 0; i < len; i++) {
            if (nums[i] <= len) { result.add(i + 1); }
        }
        
        return result;
    }
}