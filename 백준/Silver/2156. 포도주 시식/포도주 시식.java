import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       int n = Integer.parseInt(br.readLine());
       int[] dp = new int[n+1];
       int[] a = new int[n+1];
       for(int i =1; i<n+1;i++){
        a[i] = Integer.parseInt(br.readLine());
       }
       if(n > 0){
        dp[1] = a[1];
       }
       if(n>1){
        dp[2] = a[2] + a[1];
       }
       if(n>2){
        dp[3] = Math.max(Math.max(a[3]+a[2],a[3]+a[1]), dp[2]);
       }
       for(int i =4; i<n+1; i ++){
        dp[i] = Math.max(Math.max(a[i]+a[i-1]+dp[i-3], a[i]+dp[i-2]), dp[i-1]);
       }
       System.out.println(dp[n]);
    }
} 
