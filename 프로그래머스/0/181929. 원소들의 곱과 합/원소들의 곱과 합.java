class Solution {
    public int solution(int[] num_list) {
        int gob = 1;
        int plus = 0;
        for(int i : num_list){
            gob *= i;
            plus += i;
        }
        System.out.println(gob+"/"+plus);
        return gob > plus*plus ? 0:1 ;
    }
}