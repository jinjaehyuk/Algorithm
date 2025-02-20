class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] dp = new int [10000];

        for(int i = 1; i <= n; i ++){
            int tmp = 0;
            for(int j = i; j <=n; j ++){
                tmp += j;
                if(tmp == n ){
                    answer++;
                    break;
                }
                if(tmp > n){
                    break;
                }
            }
        }
        
        
        return answer;
    }
}