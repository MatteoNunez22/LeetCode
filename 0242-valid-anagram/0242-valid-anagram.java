class Solution {
    public boolean isAnagram(String s, String t) {
        int[] sMap = new int[26];
        int[] tMap = new int[26];
        
        for (char c : s.toCharArray()) {
            sMap[c - 'a']++;
        }
        
        for (char c : t.toCharArray()) {
            tMap[c - 'a']++;
        }
        
        return Arrays.equals(sMap, tMap);
    }
}