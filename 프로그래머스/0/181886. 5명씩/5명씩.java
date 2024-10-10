class Solution {
    public String[] solution(String[] names) {
        String[] answer = new String[(names.length + 4)/5];
        
        answer[0] = names[0];
        for(int i =1; i < answer.length ; i ++){
            answer[i] = names[i*5];
        }
        return answer;
    }
}