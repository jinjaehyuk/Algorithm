class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean[] sosu = new boolean[n+1];
        for(int i =2; i<=n; i ++){
            sosu[i] = true;//2~n 번째 수를 true로 초기화
        }
        //제곱근 구하기
        int root = (int)Math.sqrt(n);
        
        for(int i = 2; i <= root; i++){
            if(sosu[i]==true){
                for(int j=i; i*j<=n; j ++)
                    sosu[i*j] = false;
            }
        }
        for(int i =2; i <=n; i ++){
            if(sosu[i] == true)
            answer++;
        }
        return answer;
    }
}