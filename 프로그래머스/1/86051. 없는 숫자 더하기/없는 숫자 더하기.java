import java.util.*;
class Solution {
    public int solution(int[] numbers) {
        int totalSum = 0;
        int numSum = 0;
        
        for(int i=0; i<10; i ++){
            totalSum += i;
        }
        
        for(int i : numbers){
            numSum += i;
        }
        
        return totalSum - numSum;
    }
}