import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
       int cnt = 0;
       
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       while(true){
        int n = Integer.parseInt(br.readLine());
        if(n == 0){
            break;
        }
        cnt++;
        int[][] a= new int[n][3];
        int[][] dp= new int[n][3];
        for(int i =0;i<n;i ++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for(int j =0; j<3;j++){
                a[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp[0] = a[0];
        int start = dp[0][1];
        dp[0][2] += start;
        dp[1][0] = start + a[1][0];
        dp[1][1] +=  Math.min(Math.min(start+a[1][1], dp[1][0]+a[1][1]), dp[0][2]+a[1][1]);
        dp[1][2] +=  Math.min(Math.min(start+a[1][2], dp[1][1]+a[1][2]), dp[0][2]+a[1][2]);
        for(int i =2; i<n;i++){
            for(int j=0;j<3;j++){
                if(j==0){
                    dp[i][j] = Math.min(dp[i-1][j] + a[i][j], dp[i-1][j+1] + a[i][j]);
                }else if(j==1){
                    dp[i][j] = Math.min(Math.min(Math.min(dp[i-1][j-1] + a[i][j], dp[i-1][j] + a[i][j]), dp[i][j-1]+a[i][j]),dp[i-1][j+1]+a[i][j]);
                }else{
                    dp[i][j] = Math.min(Math.min(Math.min(dp[i-1][j-1] + a[i][j], dp[i-1][j] + a[i][j]), dp[i][j-1]+a[i][j]),dp[i-1][j-1]+a[i-1][j]+a[i][j]);
                }
            }
        }
        System.out.printf("%d. %d\n",cnt,dp[n-1][1]);
       }
    }
} 