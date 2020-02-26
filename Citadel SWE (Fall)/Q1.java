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
     * Complete the 'minimumGroups' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY predators as parameter.
     */

    public static int minimumGroups(List<Integer> predators) {
    // Write your code here
        int len = predators.size();
        int maxLvs = 1;
        HashMap<Integer, Integer> visited = new HashMap<>();

        for (int i = 0; i < len; i++) {
            int curLv = 1;
            int curPred = predators.get(i);

            if (visited.containsKey(curPred)) {
                curLv = visited.get(curPred) + 1;
            } else {
                int additionalLv = 1;
                while (!visited.containsKey(curPred) && curPred != -1) {
                    additionalLv++;
                    curPred = predators.get(curPred);
                }
                if (curPred == -1) {
                    curLv = additionalLv;
                } else {
                    curLv = additionalLv + visited.get(curPred);
                }
            }
            maxLvs = Math.max(maxLvs, curLv);
            visited.put(i, curLv);
        }

        return maxLvs;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int predatorsCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> predators = IntStream.range(0, predatorsCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        int result = Result.minimumGroups(predators);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
