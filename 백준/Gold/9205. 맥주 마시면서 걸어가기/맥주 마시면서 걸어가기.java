import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int t, n;
    static int home_x, home_y;//집 x,y
    static int[][] graph; 
    static int store_x,store_y; //상점 x,y
    static int festival_x,festival_y; //페스티벌 x,y
    static int new_x,new_y;
    static boolean[] visited;
    static StringTokenizer st;
    static Queue<int[]> queue;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        for(int i=0; i< t; i ++){
            n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            home_x = Integer.parseInt(st.nextToken());
            home_y = Integer.parseInt(st.nextToken());
            graph = new int[n][2];
            for(int j =0; j< n; j ++){
                st = new StringTokenizer(br.readLine());
                store_x = Integer.parseInt(st.nextToken());
                store_y = Integer.parseInt(st.nextToken());
                graph[j][0] = store_x;
                graph[j][1] = store_y;
            }
            st = new StringTokenizer(br.readLine());
            festival_x = Integer.parseInt(st.nextToken());
            festival_y = Integer.parseInt(st.nextToken());
            visited = new boolean[n+1];
            bfs();
        }
    }

    public static void bfs(){
        queue = new LinkedList<int[]>();
        queue.add(new int[] {home_x, home_y});
        while(!queue.isEmpty()){
            int x = queue.peek()[0];
            int y = queue.peek()[1];
            queue.poll();
            if(Math.abs(festival_x - x) + Math.abs(festival_y - y) <= 1000){
                System.out.println("happy");
                return;
            }
            for(int i =0; i < n; i ++){
                if(!visited[i]){
                    new_x = graph[i][0];
                    new_y = graph[i][1];
                    if(Math.abs(new_x - x) + Math.abs(new_y - y) <= 1000){
                        visited[i] = true;
                        queue.add(new int[] {new_x, new_y});
                    }
                }
            }
        }
        System.out.println("sad");
        return;
    }
} 
