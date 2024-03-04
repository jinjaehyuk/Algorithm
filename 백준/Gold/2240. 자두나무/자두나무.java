import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int[] arr = new int[t+1];
        for(int i=1; i<arr.length;i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        int[][] dp = new int[t+1][w+1];
        for(int i =1; i<t+1;i++){
            if(arr[i] == 1){
                dp[i][0] = dp[i-1][0] + 1;
            }else{
                dp[i][0] = dp[i-1][0];
            }
            for(int j =1;j<w+1;j++){
                if(arr[i] == 2 && j%2 == 1){
                    dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j])+1;
                }else if(arr[i] == 1 && j%2 ==0){
                    dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j])+1;
                }else{
                    dp[i][j] = Math.max(dp[i-1][j-1],dp[i-1][j]);
                }
            }
        }
        int max =0;
        for(int i = 0; i<dp[t].length; i ++){
            if(dp[t][i] > max) {
                max = dp[t][i];
            }
        }
        System.out.println(max);
    }
} 
