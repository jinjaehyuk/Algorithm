import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;
class Solution {
    static final SimpleDateFormat SDF = new SimpleDateFormat("HH:mm");
    static final String LAST_TIME= "23:59";

    public int[] solution(int[] fees, String[] records) {
        String[][] memo = new String[records.length][3]; //입/출차 기록 
        HashMap<Integer,String> manage = new HashMap<Integer, String>(); // 입 출차 관리 맵
        TreeMap<Integer, Integer> useTime = new TreeMap<Integer, Integer>();//최종 사용 시간 맵
        //입출차 기록
        for(int i =0; i< records.length; i ++){
            memo[i] = records[i].split(" ");
        }
        
        //입 출차 관리
        for(int i =0; i < memo.length; i ++){
            if(memo[i][2].equals("IN")){
                manage.put(Integer.parseInt(memo[i][1]),memo[i][0]);
            }
            else if(memo[i][2].equals("OUT")){
                int minutes = timeCal(manage.get(Integer.parseInt(memo[i][1])),memo[i][0]);

                //최종 시간 계산
                if( useTime.containsKey(Integer.parseInt(memo[i][1])) ){
                    useTime.put(Integer.parseInt(memo[i][1]), useTime.get(Integer.parseInt(memo[i][1])) + minutes);
                }
                else{
                    useTime.put(Integer.parseInt(memo[i][1]), minutes);

                }

               //출차된 차 기록삭제
                manage.remove(Integer.parseInt(memo[i][1]));
            }
        }
        if(!manage.isEmpty()){
            Set<Integer> keySet = manage.keySet();
            for(Integer key : keySet){
                int addTime = timeCal(manage.get(key),LAST_TIME);
                if(!useTime.containsKey(key)){
                    useTime.put(key, addTime);
                }else{
                    useTime.put(key, useTime.get(key) + addTime);
                }
            }
        }
        int[] answer = new int[useTime.size()];
        Set<Integer> carNums = useTime.keySet();
        int answerIdx =0;
        for(Integer carNum : carNums){
            int totalMin = useTime.get(carNum);
            if(fees[0] >= totalMin){
                answer[answerIdx] = fees[1];
            }else if ( fees[0] < totalMin){
                answer[answerIdx] = fees[1] + (int)Math.ceil((totalMin - fees[0]) / (double)fees[2]) * fees[3] ;
            }
            answerIdx ++;
        }
        
        return answer;
    }

    //A = 입차시간
    //B = 출차시간
    static public int timeCal(String A, String B){
        Date dateA = null;
        Date dateB = null;
        //출차 시 계산
        try{
            dateA = SDF.parse(A); //입차시간
            dateB = SDF.parse(B); //출차시간
        }catch (ParseException e){
            e.printStackTrace();
        }
        long differenceInMilliseconds = dateB.getTime() - dateA.getTime();
        int minutes = (int)differenceInMilliseconds / (60 * 1000); //출차까지 걸린 시간 분으로 변환

        return minutes;
    }
} 
