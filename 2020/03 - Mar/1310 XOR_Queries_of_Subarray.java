class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {

        """
        Runtime: 1 ms, faster than 100.00% of Java online submissions for XOR Queries of a Subarray.
        Memory Usage: 54.4 MB, less than 100.00% of Java online submissions for XOR Queries of a Subarray.
        """
        // Uses the property that a ^ a = 0 and a ^ 0 = a
        int len = arr.length;
        int[] pre = new int[len + 1];
        int cur = 0;
        pre[0] = 0;
        for (int i = 0; i < len; i++) {
            cur ^= arr[i];
            pre[i+1] = cur;
        }
        
        int result_len = queries.length;
        int[] result = new int[result_len];
        for (int i = 0; i < result_len; i++) {
            int[] pair = queries[i];
            result[i] = (pre[pair[0]]) ^ (pre[pair[1] + 1]);
        }
        
        return result;
    }
}