import static java.lang.Math.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        
        double sqrtN = sqrt(n);
        
        if(sqrtN %1 == 0){
            answer = (long)pow(sqrtN+1,2);
        }else{
            answer = -1;
        }
        
        return answer;
    }
}