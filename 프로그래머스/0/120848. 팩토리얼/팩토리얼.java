class Solution {
    public int solution(int n) {
        int answer = 1;
        int[] arr = new int[10];
        
        arr[0] = 1;
        for(int i =1; i < arr.length; i ++){
            arr[i] = arr[i-1] * (i+1);
            if( arr[i] <= n && n != 1){
                answer = i+1;
            }
        }
        return answer;
    }
}