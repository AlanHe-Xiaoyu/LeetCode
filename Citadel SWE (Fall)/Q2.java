import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;


class Result {

    /*
     * Complete the 'palindrome' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING s as parameter.
     */

    public static int palindrome(String s) {
    // Write your code here
        HashSet<String> result = new HashSet<>();
        int len = s.length();
        int[][] dp = new int[len][len]; // 1 yes; 0 no

        // Base case length 1
        for (int i = 0; i < len; i++) {
            dp[i][i] = 1;
            result.add(s.substring(i, i+1));
        }

        // length 2
        for (int i = 0; i < len - 1; i++) {
            if (s.charAt(i) == s.charAt(i+1)) {
                dp[i][i+1] = 1;
                result.add(s.substring(i, i+2));
            } else {
                dp[i][i+1] = 0;
            }
        }

        // DP starts
        for (int curLen = 3; curLen <= len; curLen++) {
            for (int start = 0; start < len - curLen + 1; start++) {
                int end = start + curLen - 1;
                // 'x' + DP[][] + 'x'
                if (s.charAt(start) == s.charAt(end) && dp[start+1][end-1] == 1) {
                    dp[start][end] = 1;
                    result.add(s.substring(start, end+1));
                } else {
                    dp[start][end] = 0;
                }
            }
        }

        return result.size();
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        int result = Result.palindrome(s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
