import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n+1];
        int[][] tp = new int[n][2];
        for(int i =0; i<n; i ++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            tp[i][0] = t;
            tp[i][1] = p;
        }
        for(int i =0; i < n; i++){
            for(int j=i+tp[i][0]; j<n+1;j++){
                if(dp[j] < dp[i] + tp[i][1]){
                    dp[j] = dp[i] + tp[i][1];
                }
            }
        }
        System.out.println(dp[n]);            
    }   
} 