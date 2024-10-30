class Solution {
    public int solution(String myString, String pat) {
        myString = myString.toUpperCase();
        pat = pat.toUpperCase();
        
        return myString.indexOf(pat) > -1? 1 : 0;
    }
}