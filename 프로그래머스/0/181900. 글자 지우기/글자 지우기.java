import java.util.*;
class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        String[] arr_s = my_string.split("");
        for(int i = 0; i< indices.length; i ++){
            arr_s[indices[i]] = "";
        }
        
        for(int i =0 ;i<arr_s.length; i++){
            if(arr_s[i] == ""){
                continue;
            }else{
                answer += arr_s[i];
            }
        }
        
        return answer;
    }
}