import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int num = n;
        int cnt =0;
        while(true){
            int A = num / 10;
            int B = num % 10;
            int C = (A + B) % 10;
            num = (B*10) + C;
            cnt += 1;
            if(n == num){
                System.out.println(cnt);
                break;
            }
        }
    }
} 