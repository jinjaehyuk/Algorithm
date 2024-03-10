import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int MAX_NUM = 10;
    static int mod = 10007;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] dp = new long[MAX_NUM];
        for(int i =0; i < MAX_NUM;i++){
            dp[i] = 1;
        }
        for(int i =1; i<n; i++){
            for(int j = 1; j<MAX_NUM;j++){
                dp[j] += (dp[j-1]%mod);
            }
        }
        long sum =0;
        for(int i =0; i < MAX_NUM;i++){
            sum += dp[i];
        }
        System.out.println(sum%mod);
    }   
} 