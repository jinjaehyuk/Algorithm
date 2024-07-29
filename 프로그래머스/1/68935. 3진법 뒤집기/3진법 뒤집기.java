class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String thr = Integer.toString(n,3);
        String temp = "";
        for(int i =thr.length()-1; i>-1; i --){
            temp += thr.charAt(i);
        }
        
        answer = Integer.parseInt(temp,3);
        
        return answer;
    }
}