import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    static int[] dpZero;
    static int[] dpOne;
    static int MAX_NUM = 41;
    public static void main(String[] args) throws IOException{
        dpZero = new int[MAX_NUM];
        dpOne = new int[MAX_NUM];
        dpZero[0] = 1;
        dpOne[0] = 0;
        dpZero[1] = 0;
        dpOne[1] = 1;
        for(int i =2; i< MAX_NUM; i ++){
            dpZero[i] = dpZero[i-1] + dpZero[i-2];
            dpOne[i] = dpOne[i-1] + dpOne[i-2];
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int i =0; i < t; i++){
            int n = Integer.parseInt(br.readLine());
            System.out.print(dpZero[n] + " " + dpOne[n]);
            System.out.println();
        }
    }
} 