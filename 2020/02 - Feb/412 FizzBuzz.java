class Solution {
    public List<String> fizzBuzz(int n) {
        
        """
        Runtime: 1 ms, faster than 99.89% of Java online submissions for Fizz Buzz.
        Memory Usage: 41.7 MB, less than 5.40% of Java online submissions for Fizz Buzz.
        """
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 3 != 0 && i % 5 != 0) {
                result.add(Integer.toString(i));
            } else if (i % 3 != 0) {
                result.add("Buzz");
            } else if (i % 5 != 0) {
                result.add("Fizz");
            } else {
                result.add("FizzBuzz");
            }
        }
        
        return result;
    }
}