import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class PointXYZ{
    int height;
    int row;
    int col;

    public PointXYZ(int height, int row, int col){
        this.height = height;
        this.row = row;
        this.col = col;

    }
}

public class Main {
    static final int[] dx = {-1,1,0,0,0,0};
    static final int[] dy = {0,0,-1,1,0,0};
    static final int[] dz = {0,0,0,0,-1,1};
    static StringTokenizer st;
    static Queue<PointXYZ> queue = new LinkedList<PointXYZ>();
    static int n;
    static int m;
    static int h;
    static int[][][]  tomato;
    public static void main(String[] args) throws IOException {
        BufferedReader br=  new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        
        tomato = new int[h][n][m];
        for(int z =0; z < h; z ++){
            for(int i = 0; i < n; i ++){
                st = new StringTokenizer(br.readLine());
                for (int j =0; j < m; j ++){
                    tomato[z][i][j] = Integer.parseInt(st.nextToken());
                }
            }
        }
        for(int z =0; z < h; z ++){
            for(int i = 0; i < n; i ++){
                for (int j =0; j < m; j ++){
                    if(tomato[z][i][j] == 1) queue.add(new PointXYZ(z,i,j));
                }
            }
        }
        System.out.println(bfs());
    }

    private static int bfs(){
        while(!queue.isEmpty()){
            PointXYZ point = queue.poll();
            int z = point.height;
            int x = point.row;
            int y = point.col;
            for(int i =0; i < 6; i ++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                int nz = z + dz[i];
                if( 0<= nx && nx<n && 0<=ny && ny<m && 0<= nz && nz< h  && tomato[nz][nx][ny] == 0){
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1;
                    queue.add(new PointXYZ(nz,nx,ny));
                }
            }
        }
        int max_value = 0;
        boolean flag = false;
        for(int z = 0; z<h; z ++){
            for( int i =0; i< n; i ++){
                for(int j=0; j< m; j ++){
                    if(tomato[z][i][j] == 0){
                        flag = true;
                        break;
                    }
                    if(max_value < tomato[z][i][j]){
                        max_value = tomato[z][i][j];
                    }
                }
            }
        }
        int result = 0;
        if(flag){
            result = -1;
        }else{
            result = max_value-1;
        }
        return result;
    }
} 
