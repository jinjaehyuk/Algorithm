class Solution {
    public int solution(int n) {
        int answer = 0;
        String[] nn = String.valueOf(n).split("");
        
        for(int i =0; i< nn.length; i++){
            answer +=Integer.parseInt(nn[i]);
        }     
        return answer;
    }
}