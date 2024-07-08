import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
                
        ArrayList<Integer> aList= new ArrayList<>();
       
        aList.add(arr[0]);
        for(int i = 1; i < arr.length; i ++){
           if(arr[i] != arr[i-1]){
               aList.add(arr[i]);
           } 
        }
        answer = new int[aList.size()];
        for(int i =0; i<answer.length; i ++){
            answer[i] = aList.get(i);
        }
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

        return answer;
    }
}