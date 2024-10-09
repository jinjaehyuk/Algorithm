class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int sumA = 0;
        int sumB = 0;
        sumA = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        sumB = Integer.parseInt(String.valueOf(b) + String.valueOf(a));

        
        
        return sumA > sumB ? sumA: sumB;
    }
}