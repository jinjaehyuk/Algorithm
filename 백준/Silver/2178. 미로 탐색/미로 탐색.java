import java.io.IOException;

import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    static final int[] DX = {0,0,-1,1};
    static final int[] DY = {-1,1,0,0};
    static int n;
    static int m;
    static int[][] nm;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        nm = new int[n][m];
        for(int i =0; i < n; i ++){
            String s = br.readLine();
            for(int j =0; j <m; j ++){
                nm[i][j] = s.charAt(j)-'0';
            }
        }   
        bfs(0,0);
        System.out.println(nm[n-1][m-1]);
    }
    public static void bfs(int x, int y){
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {x,y});
        while(!q.isEmpty()){
            int[] now = q.poll();
            int nowX = now[0];
            int nowY = now[1];
            for(int i =0; i < 4; i ++){
                int nx = nowX+ DX[i];
                int ny = nowY+ DY[i];
                if( (0<= nx && nx < n) && (0<= ny && ny < m ) && nm[nx][ny] == 1){
                    nm[nx][ny] = nm[nowX][nowY] + 1;
                    q.add(new int[] {nx,ny});
                }
            }
        }
    } 
} 