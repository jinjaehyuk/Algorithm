import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static StringTokenizer st;
    public static int[][] graph;
    public static int[][] dp;
    public static int y1,x1,y2,x2;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        graph = new int[n+1][n+1];
        for(int i=1; i < n+1; i ++){
            st = new StringTokenizer(br.readLine());
            for(int j=1; j<n+1; j ++){
                graph[i][j]= Integer.parseInt(st.nextToken());
            }
        }
        dp = new int[n+1][n+1];
        for(int i=1;i<n+1;i++){
            for(int j=1;j<n+1;j++){
                dp[i][j] = graph[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];
            }
        }
        for(int i=0; i<m; i ++){
            st = new StringTokenizer(br.readLine());
            y1 = Integer.parseInt(st.nextToken());
            x1 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            System.out.println(dp[y2][x2] - dp[y1-1][x2] - dp[y2][x1-1]+dp[y1-1][x1-1]);
        }
    }
} 
