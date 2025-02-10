class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        
        String[] t_arr = t.split("");
        String[] p_arr = p.split("");
        int i =0;
        
        while(i < t_arr.length-p_arr.length+1){
            String tmp = "";
            for(int j =i; j < p_arr.length+i; j ++){
                tmp += t_arr[j];
            }
            
            if(Long.parseLong(p) >= Long.parseLong(tmp)){
                answer++;
            }
            i++;
        }
        
        
        
        return answer;
    }
}