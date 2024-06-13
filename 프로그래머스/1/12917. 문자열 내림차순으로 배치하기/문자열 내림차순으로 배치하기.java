import java.util.*;
import java.lang.StringBuilder;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        char[] charS = s.toCharArray();      
        Arrays.sort(charS);
        return new StringBuilder(new String(charS)).reverse().toString();
    }
}