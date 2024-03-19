import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    static int leftArm = 0;
    static int rightArm = 0;
    static int waist = 0;   //허리
    static int leftLeg = 0;
    static int rightLeg = 0;
    static int heartX = 0; //심장좌표
    static int heartY = 0; //심장좌표
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[][] cookieBody = new String[n][n];
        for(int i =0; i < n; i ++ ){
            cookieBody[i] = br.readLine().split("");
        }  

        for(int i =0; i < n; i ++){
            for(int j = 0; j<n ; j++){
                if(heartX ==0 && heartY ==0 ){ //머리
                    if(cookieBody[i][j].equals("*")){    //머리
                        heartX = i+1;
                        heartY = j;
                    }
                }else if(i == heartX){
                   if(cookieBody[i][j].equals("*")){
                        if(j < heartY ){
                            leftArm ++;
                        }else if(j > heartY){
                            rightArm ++;
                        }
                    }
                }else{
                    if(j == heartY && cookieBody[i][j].equals("*")){ //허리
                        waist ++;
                    }else{
                        if(j == heartY-1 && cookieBody[i][j].equals("*")){
                            leftLeg ++;
                        }else if(j == heartY+1 && cookieBody[i][j].equals("*")){
                            rightLeg ++;
                        }
                    }

                }

            }
        }
        System.out.println((heartX+1) +" " + (heartY+1));
        System.out.println(leftArm + " " + rightArm+" "+waist+" "+leftLeg+" "+rightLeg);
    }
} 
