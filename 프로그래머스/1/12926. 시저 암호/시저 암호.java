class Solution {
    public String solution(String s, int n) {
       char[] enc = new char[s.length()];
		
		for(int i=0; i<s.length(); i++) {
			char ch = s.charAt(i);
			if(Character.isLowerCase(ch)) {
				ch = (char)((ch - 'a' + n) % 26 + 'a');
			}else if(Character.isUpperCase(ch)) {
				ch = (char)((ch - 'A' + n) % 26 + 'A');
			}
			enc[i] = ch;
		}
		
        return String.valueOf(enc); 
    }
}