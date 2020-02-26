class Solution {
    public int maxArea(int[] height) {

        """
        Runtime: 1 ms, faster than 100.00% of Java online submissions for Container With Most Water.
        Memory Usage: 41.1 MB, less than 13.46% of Java online submissions for Container With Most Water.
        """
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;
        
        while (left < right) {
            if (height[left] < height[right]) {
                maxArea = Math.max(maxArea, height[left] * (right - left));
                left++;
            } else {
                maxArea = Math.max(maxArea, height[right] * (right - left));
                right--;
            }
        }
        
        return maxArea;
    }
}