class Solution {
    public int solution(int[] sides) {
        int max = sides[0];
        int answer = sides[1] + sides[2];

        if(max <sides[1]){
            max = sides[1];
            answer = sides[0] + sides[2];
        }
        if(max < sides[2]){
            max = sides[2];
            answer = sides[0]+sides[1];
        }
        return max < answer ? 1 : 2;
    }
}