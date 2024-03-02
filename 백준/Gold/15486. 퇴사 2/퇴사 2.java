import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n+1];
        int[][] tp = new int [n][2];
        StringTokenizer st = null;
        for(int i =0; i < n; i ++){
            st =  new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            tp[i][0] = a;
            tp[i][1] = b;
        }
        for(int i =0; i <n; i ++){
            dp[i+1] = Math.max(dp[i+1],dp[i]);

            if(i+tp[i][0] <= n){
                dp[i+tp[i][0]] = Math.max(dp[i+tp[i][0]], dp[i] + tp[i][1]);
            }
        }
        System.out.println(dp[n]);
    }
} 