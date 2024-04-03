import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int n,a,b,m,x,y;
    static StringTokenizer st;
    static List<Integer>[] rel;
    static int[] visited;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(br.readLine());
        
        rel = new ArrayList[n+1];
        for(int i =1; i<n+1; i ++){
            rel[i] = new ArrayList<>();
        }
        visited = new int[n+1];
        for(int i =0; i< m; i ++){
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            rel[x].add(y);
            rel[y].add(x);
        }
        bfs(Math.min(a,b));
        System.out.println(visited[Math.max(a,b)] - visited[Math.min(a,b)]);
    }

    public static void bfs(int v){
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(v);
        visited[v] = 1;
        while(!queue.isEmpty()){
            x = queue.poll();
            for(int i : rel[x]){
                if(visited[i] == 0){
                    queue.add(i);
                    visited[i] = visited[x] + 1;
                }
            }
        }
    }
} 
