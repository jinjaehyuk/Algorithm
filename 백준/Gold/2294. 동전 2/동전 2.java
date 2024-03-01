import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] token = br.readLine().split(" ");
        int n = Integer.parseInt(token[0]);
        int k = Integer.parseInt(token[1]);
        int[] coins = new int[n];
        for(int i =0; i < n; i++){
            coins[i] = Integer.parseInt(br.readLine());
        }
        int[] dp = new int[k+1];
        for(int x=1 ; x<dp.length;x++){
            dp[x] = 10001;
        }
        dp[0] = 0;
        for(int coin:coins){
            for(int j = coin;j<k+1; j++){
                if(dp[j] > 0){
                    dp[j] = Math.min(dp[j], dp[j-coin]+1);
                }
            }
        }
        System.out.println(dp[k] == 10001 ? -1 : dp[k]);
    }
} 