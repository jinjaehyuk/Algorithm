class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        
        int i = 0;
        int sum = 0;
        
        while(i < count){
            i++;
            sum += price;
            answer += sum;
        }
        
        return answer - money  >= 0 ? answer - money : 0 ;
    }
}