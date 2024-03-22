import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[][] dp;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        dp = new int[n][3];
       
        for(int i =0; i < n; i ++){
            st = new StringTokenizer(br.readLine());
            for(int j =0; j<3; j++){
                dp[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for(int i =1; i < n; i ++){
            for(int j =0; j<3; j++){
                if(j==0){
                    dp[i][j] = Math.min(dp[i-1][j+1]+dp[i][j], dp[i-1][j+2]+dp[i][j]);
                }else if(j ==1){
                    dp[i][j] = Math.min(dp[i-1][j-1]+dp[i][j], dp[i-1][j+1]+dp[i][j]);
                }else{
                    dp[i][j] = Math.min(dp[i-1][j-2]+dp[i][j], dp[i-1][j-1]+dp[i][j]);
                }
            }
        }
        int min_value = dp[n-1][0];
        for(int i=1; i< 3; i ++){
            if(dp[n-1][i] < min_value){
                min_value = dp[n-1][i];
            }
        }
        System.out.println(min_value);
    }
} 