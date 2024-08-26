class Solution {
    public int[] solution(int start_num, int end_num) {
        int length = start_num - end_num+1 ;
        int[] answer = new int[length];
        answer[0] = start_num;
        for(int i = 1; i < length; i ++){
            start_num --;
            answer[i] = start_num;
            
        }
        
        return answer;
    }
}