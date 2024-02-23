import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       int n = Integer.parseInt(br.readLine());
       StringTokenizer st = new StringTokenizer(br.readLine());
       int[] dp = new int[n];
       int[] a = new int[n];
       for(int i =0; st.hasMoreTokens();i++){
        a[i] = Integer.parseInt(st.nextToken());
       }
       dp[0] = a[0];
       int max = a[0];
       for(int i =1; i < n; i ++){
        dp[i] = Math.max(a[i], dp[i-1] + a[i]);
        max = Math.max(max,dp[i]);
       }
       System.out.println(max);
    }
} 
