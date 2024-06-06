import java.util.*;
class Solution {
    public long solution(long n) {
        long answer = 0;
        
        String[] arrSnum = String.valueOf(n).split("");
        int[] arrInum = new int[arrSnum.length];
        String num = "";
        
        Arrays.sort(arrSnum, Collections.reverseOrder());
        
        for(String i: arrSnum){
            num += i;
        }
        return Long.parseLong(num);
    }
}