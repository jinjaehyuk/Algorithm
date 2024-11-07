
import java.util.*;
class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        String[] arr = cipher.split("");
        List<String> list = new ArrayList<>();
        list.add("");
        for(int i =0; i<arr.length; i ++){
            list.add(arr[i]);
        }
        for(int i =1; i < list.size(); i ++){
            if(i%code == 0){
                answer += list.get(i);
            }
        }
        
        return answer;
    }
}