import java.util.*;
class Solution {
    public String[] solution(String[] strArr) {
        List<String> list = new ArrayList<>();
        int num =0;
        for(int i =0; i < strArr.length; i ++){
            if(!strArr[i].contains("ad")){
                list.add(strArr[i]);
                num ++;
            }
        }
        String[] answer = new String[num];
        for(int i =0; i< list.size(); i++){
            answer[i] = list.get(i);
        }

        return answer;
    }
}