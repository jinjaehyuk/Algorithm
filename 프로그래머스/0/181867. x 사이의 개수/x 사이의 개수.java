class Solution {
    public int[] solution(String myString) {
        
        String[] arr = myString.split("x");
        int[] answer = null;
        if(myString.substring(myString.length()-1, myString.length()).equals("x")){
            answer = new int[arr.length+1];
        }else{
            answer = new int[arr.length];
        }
       
        for( int i =0; i<arr.length; i ++){
            answer[i] = arr[i].length();
            
        }
        
        return answer;
    }
}