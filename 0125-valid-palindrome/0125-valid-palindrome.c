bool isPalindrome(char * s){
    int size = strlen(s);
    if (size == 1) return true;
    
    int l = 0;
    int r = size - 1;
    
    while (l < r) {
        if (isalnum(s[l]) && isalnum(s[r])) {
            char c_l = tolower(s[l]);
            char c_r = tolower(s[r]);
            
            if (c_l != c_r) return false;
            
            l++;
            r--;
        }
        
        if (!isalnum(s[l])) l++;
        if (!isalnum(s[r])) r--;
            
    }
    
    return true;
    
}