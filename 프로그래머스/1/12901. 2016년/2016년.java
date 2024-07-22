import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.HashMap;

class Solution {
    public String solution(int a, int b) {
        String answer = "";
        
        LocalDate date = LocalDate.of(2016,a,b);
        DayOfWeek dayOfWeek = date.getDayOfWeek();
        
        HashMap<Integer, String> days = new HashMap<Integer,String>();
        
        days.put(1,"MON");
        days.put(2,"TUE");
        days.put(3,"WED");
        days.put(4,"THU");
        days.put(5,"FRI");
        days.put(6,"SAT");
        days.put(7,"SUN");
        
        answer = days.get(dayOfWeek.getValue());
        
        return answer;
    }
}
