import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
    
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a= new int[n];
        int[] dp= new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i =0; i< n; i ++){
            a[i] = Integer.parseInt(st.nextToken());
            dp[i] = 1;
        }
        
        for(int i =0; i< n; i ++){
            for(int j=i; j<n; j++){
                if(a[i] < a[j]){
                    dp[j] = Math.max(dp[j], dp[i]+1);
                }
            }
        }
        int maxCnt = 0;
        for(int i =0; i < n; i ++){
            if(dp[i] > maxCnt){
                maxCnt = dp[i];
            }
        }
        System.out.println(maxCnt); 
    }
}