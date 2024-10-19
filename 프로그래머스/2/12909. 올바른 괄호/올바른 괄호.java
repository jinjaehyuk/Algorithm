import java.util.*;
class Solution {
    boolean solution(String s) {        
        if(s.charAt(0) == ')') return false;
        
        Stack<Character> stack = new Stack<>();
        
        try{
            for(char c: s.toCharArray()){
                if(c=='(') stack.push(c);
                else if(c==')') stack.pop();
            }
        }catch(Exception e){
            return false;
        }
        
        return stack.size() ==0? true: false;
    }
}