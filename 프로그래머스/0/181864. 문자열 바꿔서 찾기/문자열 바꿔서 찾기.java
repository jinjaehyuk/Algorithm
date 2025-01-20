class Solution {
    public int solution(String myString, String pat) {
        String answer = "";
        for(int i = 0; i < myString.length(); i++) {
            if(String.valueOf(myString.charAt(i)).equals("A")) {
                answer += "B";
            } else {
                answer += "A";
            }
        }
        if(answer.contains(pat)) return 1;
        return 0;
    }
}