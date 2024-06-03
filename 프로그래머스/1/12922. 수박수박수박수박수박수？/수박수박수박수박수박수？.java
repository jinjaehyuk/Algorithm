class Solution {
    public String solution(int n) {
        String answer = "";
        String su = "수";
        String park = "박";
        
        for(int i =1; i <= n; i ++){
            if(i%2 == 0){
                answer += park;
            }else{
                answer += su;
            }
        }
        
        
        return answer;
    }
}