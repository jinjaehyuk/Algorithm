import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        ArrayList<Integer> arrList = new ArrayList<>();
        for(int num : arr){
            if(num % divisor == 0){
                arrList.add(num);
            }
        }

        if(arrList.size() == 0){
            answer = new int[]{-1};
        }else{
            int cnt = 0;
            answer = new int[arrList.size()];
            for(int temp : arrList){
                answer[cnt++] = temp;
            }
            Arrays.sort(answer);
        }
        return answer;
    }
}