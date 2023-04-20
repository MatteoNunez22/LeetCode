bool isAnagram(char * s, char * t){
    
    int i;
    int freq[26] = {0};
    
    for (i = 0; s[i] != NULL; i++) {
        char c = s[i] - 'a';
        freq[c]++;
    }
    
    for (i = 0; t[i] != NULL; i++) {
        char c = t[i] - 'a';
        freq[c]--;
        if (freq[c] < 0) return false;
    }
    
    for (i = 0; i < 26; i++) {
        if (freq[i] != 0) return false;
    }
    
    return true;
}