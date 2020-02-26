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
     * Complete the 'longestChain' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING_ARRAY words as parameter.
     */

    private static int singleWordChain(String word, HashMap<String, Integer> result) {
        if (word.length() == 1) {
            return 1;
        } else if (result.get(word) != -1) { // Done already
            return result.get(word);
        }

        int curMax = 1;
        for (int i = 0; i < word.length(); i++) {
            StringBuffer buffer = new StringBuffer(word);
            buffer.deleteCharAt(i);
            String oneLess = buffer.toString();
            if (result.containsKey(oneLess)) {
                curMax = Math.max(curMax, 1 + singleWordChain(oneLess, result));
            }
        }

        result.put(word, curMax);
        return curMax;
    }

    public static int longestChain(List<String> words) {
    // Write your code here
        if (words.size() == 0) {
            return 0;
        }

        // keeps track of answer + initialize
        HashMap<String, Integer> result = new HashMap<>();
        int globalMax = 0;
        for (String s : words) {
            result.put(s, -1);
        }

        for (String s : words) {
            // no need to check shorter words
            if (globalMax < s.length()) {
                int curMax = singleWordChain(s, result);
                globalMax = Math.max(globalMax, curMax);
            }
        }

        return globalMax;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int wordsCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> words = IntStream.range(0, wordsCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        int result = Result.longestChain(words);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
