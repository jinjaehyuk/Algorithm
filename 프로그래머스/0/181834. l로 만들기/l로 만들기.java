class Solution {
    public String solution(String myString) {
        String answer = "";

        for(char x: myString.toCharArray()){
            if(x < 108){
                x = 108;
            }
            answer += x; 
        }
        return answer;
    }
}