class Solution {
    public int maxProfit(int[] prices) {

        """
        Runtime: 1 ms, faster than 91.80% of Java online submissions for Best Time to Buy and Sell Stock II.
        Memory Usage: 42.5 MB, less than 5.71% of Java online submissions for Best Time to Buy and Sell Stock II.
        """
        if (prices == null || prices.length <= 1) {
            return 0;
        }
        
        int result = 0;
        int buy_price = prices[0];
        for (int i = 1; i < prices.length; i++) {
            int new_price = prices[i];
            if (new_price > buy_price) { result += new_price - buy_price; }
            buy_price = new_price;
        }
        return result;
    }
}