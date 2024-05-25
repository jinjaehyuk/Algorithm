import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        //정렬
        Arrays.sort(people);
        int start = 0, end = people.length - 1;
        while(start < end){
            if(people[start] + people[end] <= limit){
                start ++;
                end --;
            }else{
                end --;
            }
            answer ++;
        }
        return start == end ? answer +1 : answer;
    }
}