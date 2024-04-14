import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static StringTokenizer st;
    public static int[] a;
    public static int[] dp;
    public static int n;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        
        a = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i =0; i<n; i++){
            a[i] = Integer.parseInt(st.nextToken());
        }
        dp = new int[n];
        dp[0] = a[0];
        for(int i =1; i<n+1; i++){
            for(int j=i; j<n; j ++){
                if(a[i-1] < a[j] ){
                    dp[j] = Math.max(dp[j],dp[i-1] + a[j]);
                }else{
                    dp[j] = Math.max(dp[j],a[j]);
                }
            }
        }
        int max_num = 0;
        for(int i =0; i<n; i ++){
            if(max_num < dp[i]){
                max_num = dp[i];
            }
        }
        System.out.println(max_num);
    }
} 