class Solution {
    public int solution(int n, String control) {
        int answer = n;
        String[] arr_con = control.split("");
        
        for(int i =0; i < arr_con.length; i ++){
            if(arr_con[i].equals("w")){
                answer += 1;
            }else if(arr_con[i].equals("s")){
                answer -= 1;
            }else if(arr_con[i].equals("d")){
                answer += 10;
            }else{
                answer -= 10;
            }
        }
        
        return answer;
    }
}