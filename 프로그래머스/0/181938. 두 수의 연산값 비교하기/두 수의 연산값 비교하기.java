class Solution {
    public int solution(int a, int b) {
        int sumA = 0;
        int sumB = 0;
        sumA = Integer.parseInt(String.valueOf(a)+String.valueOf(b));
        sumB = 2 * a * b;

        return sumA > sumB ? sumA : sumB;
    }
}