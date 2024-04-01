import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static class Point{
        int x,y,d;
        public Point(int xx, int yy, int dd){
            y = yy;
            x = xx;
            d = dd;
        }
    }

    static int n,m,r,c,d,nr,nc;
    static int[][] graph;
    static StringTokenizer st;
    static int[] dr = new int[]{-1,0,1,0};
    static int[] dc = new int[]{0,1,0,-1};
    static int cnt = 1;
    static  Queue<Point> queue;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        graph = new int[n][m];
        for(int i = 0; i<n; i ++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j ++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        queue = new LinkedList<>();
        queue.add(new Point(r,c,d));
        graph[r][c] = 2;

        bfs();
    }

    static public void bfs(){
        while(!queue.isEmpty()){
            int flag = 0;
            Point p = queue.poll();
            int x = p.x;
            int y = p.y;
            int d = p.d;
            for(int i =0; i < 4; i ++){
                d = (d+3)%4;
                nr = x +dr[d];
                nc = y + dc[d];
                if(0<=nr && nr<n && 0<= nc && nc<m && graph[nr][nc] == 0){
                    cnt +=1;
                    queue.add(new Point(nr,nc,d));
                    graph[nr][nc]=2;
                    flag = 1;
                    break;
                }
            }
            if( flag == 0){
                if(graph[x-dr[d]][y-dc[d]] == 1){
                    System.out.println(cnt);
                    break;
                }
                else{
                    queue.add(new Point(x-dr[d],y-dc[d], d));
                }
            }
        }
    } 
} 
