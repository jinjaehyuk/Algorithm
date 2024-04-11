import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] dp = new int[n][n];
        for(int i = 0 ; i < n ; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j <= i ;j++) {
				dp[i][j]=Integer.parseInt(st.nextToken());
			}
		}
        for(int i =1; i< n ;i ++){
            for(int j = 0; j <i+1;j++){
                if(i ==1){
                    dp[i][j] += dp[0][0];
                }else if(j == 0){
                    dp[i][j] += dp[i-1][j];
                }else if(j == dp[i].length-1){
                    dp[i][j] += dp[i-1][j-1];
                }else{
                    dp[i][j] += Math.max(dp[i-1][j-1], dp[i-1][j]);
                }
            }
        }
        int max =0;
        for(int i =0; i<n; i++ ){
            if(max < dp[n-1][i]){
                max = dp[n-1][i];
            }
        }
        System.out.println(max);
    }
} 
