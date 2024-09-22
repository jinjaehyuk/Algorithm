import java.util.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        Map<String,Integer> map = new HashMap<>();
        String[][] temp = new String[terms.length][terms.length];
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy.MM.dd");
        LocalDate formatToday = LocalDate.parse(today,formatter);
        List<Integer> selectedNumbers = new ArrayList<>();

      
        for(int i =0; i< terms.length; i ++){
            temp[i] = terms[i].split(" ");
            map.put(temp[i][0], Integer.parseInt(temp[i][1]));
        }
        
        
        temp = new String[privacies.length][privacies.length];
        for(int i =0; i < privacies.length; i ++){
            temp[i] = privacies[i].split(" ");
            
            LocalDate addDate = LocalDate.parse(temp[i][0], formatter);
              
            LocalDate pDate = addDate.plusMonths(map.get(temp[i][1]));
            
            if(pDate.isBefore(formatToday) || pDate.equals(formatToday)){
                selectedNumbers.add(i+1);
            }
            
        }
        int[] answer = new int[selectedNumbers.size()];
        for(int i =0; i < selectedNumbers.size(); i ++){
            answer[i] = selectedNumbers.get(i);
        }
        
        
        return answer;
    }
}