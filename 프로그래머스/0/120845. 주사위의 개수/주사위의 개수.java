class Solution {
    public int solution(int[] box, int n) {
        int answer = 0;
        answer = (int)(box[0]/n) * (int)(box[1]/n )* (int)(box[2]/n);
        return answer;
    }
}