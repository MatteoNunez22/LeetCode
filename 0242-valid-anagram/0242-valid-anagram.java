class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            if (sMap.containsKey(c)) {
                int freq = sMap.get(c);
                sMap.put(c, freq + 1);
                
            } else {
                sMap.put(c, 1);
            }
        }
        
        for (char c : t.toCharArray()) {
            if (tMap.containsKey(c)) {
                int freq = tMap.get(c);
                tMap.put(c, freq + 1);
                
            } else {
                tMap.put(c, 1);
            }
        }
        
        return sMap.equals(tMap);
    }
}