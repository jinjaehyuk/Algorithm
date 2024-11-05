class Solution {
    public String solution(int age) {
        String ageS = String.valueOf(age);
        ageS =ageS.replaceAll("0","a");
        ageS = ageS.replaceAll("1","b");
        ageS = ageS.replaceAll("2","c");
        ageS = ageS.replaceAll("3","d");
        ageS = ageS.replaceAll("4","e");
        ageS = ageS.replaceAll("5","f");
        ageS = ageS.replaceAll("6","g");
        ageS = ageS.replaceAll("7","h");
        ageS = ageS.replaceAll("8","i");
        ageS = ageS.replaceAll("9","j");

        return ageS;
    }
}