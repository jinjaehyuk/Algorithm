import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int MAX_NUM = 41;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[] vip = new int[m];
        for(int i=0; i<m;i++){
            vip[i] = Integer.parseInt(br.readLine());
        }
        int[] dp =new int[MAX_NUM];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        for(int i=3; i<MAX_NUM; i ++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        long answer = 1;
        if(m > 0){
            int pre =0;
            for(int j =0; j<m;j++){
                answer *= dp[vip[j] -1 -pre];
                pre = vip[j];
            }
            answer *= dp[n-pre];
        }else{
            answer = dp[n];
        }
        System.out.println(answer);
    }   
} 