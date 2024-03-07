import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int mod = 1000000009;
    public static void main(String[] args) throws IOException{
        long[] dp = new long[1000001];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i =4;i<dp.length;i ++){
            dp[i] = (dp[i-1]% mod + dp[i-2]% mod + dp[i-3]% mod) % mod;
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int i =0; i <t; i ++){
            int n = Integer.parseInt(br.readLine());
            System.out.println(dp[n]%mod);
        }
    }   
} 