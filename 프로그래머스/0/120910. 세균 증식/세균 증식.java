class Solution {
    public int solution(int n, int t) {
        int answer = n;
        int i = 0;
        while(i < t){
            i ++;
            answer *=  2;
        }
        return answer;
    }
}