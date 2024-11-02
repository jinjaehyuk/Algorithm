class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        int sum = 0;
        String arr = "";
        for(int i =0; i< finished.length; i ++){
            if(!finished[i]){
                sum ++;
                arr += i+",";
            }
        }
        String[] answer = new String[sum];
        String[] arr2 = arr.split(",");
        for(int i =0; i < arr2.length; i ++){
            answer[i] = todo_list[Integer.parseInt(arr2[i])];
        }
        
        return answer;
    }
}