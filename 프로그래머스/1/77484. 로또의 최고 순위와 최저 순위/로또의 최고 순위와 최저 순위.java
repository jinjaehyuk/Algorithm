import java.util.HashMap;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        HashMap<Integer, Integer> rank = new HashMap<Integer,Integer>();
        int current_num =6;
        for(int i = 1; i <=6; i ++){
            rank.put(i, current_num);
            current_num --;
        }
        int[] answer = new int[2];
        int count = 0;
        int zero_cnt = 0;
        for(int i=0; i < lottos.length; i ++){
            if(lottos[i] == 0){
                zero_cnt ++;
                continue; 
            }
            for(int j =0; j < lottos.length; j++){
                if(lottos[i] == win_nums[j]){
                    count ++;
                }
            }
        }

        answer[0] = rank.get(count+zero_cnt == 0 ? 1 : count+zero_cnt);
        answer[1] = rank.get(count == 0 ? 1 : count);

        return answer;
    }
}