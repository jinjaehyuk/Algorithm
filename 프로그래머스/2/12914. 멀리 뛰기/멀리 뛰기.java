class Solution {
    public long solution(int n) {
        long answer = 0;
        
        long[] arr = new long[2001];
        arr[0] = 0;
        arr[1] = 1;
        for(int i =2; i <arr.length; i ++){
            arr[i] = (arr[i-2] + arr[i-1])%1234567;
        }
        
        
        return arr[n+1];
    }
}