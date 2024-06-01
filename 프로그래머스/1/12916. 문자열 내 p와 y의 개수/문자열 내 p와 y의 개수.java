class Solution {
    
    
    boolean solution(String s) {
        boolean answer = true;
        int char_p = 0;
        int char_y = 0;
        s = s.toLowerCase();
        String[] arr = s.split("");
        for(int i=0; i < arr.length; i ++){
            if(arr[i].equals("p")) char_p ++;
            else if(arr[i].equals("y")) char_y ++;
        }
        if (char_p != char_y) answer =false; 
        return answer;
    }
}