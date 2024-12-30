class Solution {
    public int solution(int n) {
        int answer = 0;
        int count =Integer.bitCount(n);
        while(true){
            n ++ ;
            if(count == Integer.bitCount(n)){
                answer = n;
                break;
            }
        }
        return answer;
    }
        /*
        for(int i = n+1; i < 1000001; i ++){
            String binary = Integer.toBinaryString(i); // 10진수 -> 2진수
            countB = countChar(binary,'1');
            if(countB == countN){
                answer = i;
                break; 
            }
            
            
        }
        return answer;
    }
    public static int countChar(String str, char ch) {        
        return str.length() - str.replace(String.valueOf(ch), "").length();    
    }
    */
}