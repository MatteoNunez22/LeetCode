class Solution {
    public boolean isPalindrome(String s) {
        for (int l = 0, r = s.length() - 1; l < r; l++, r--) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) {
                l++;
            }
            
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) {
                r--;
            }
            
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
        }
        
        return true;
    }
}