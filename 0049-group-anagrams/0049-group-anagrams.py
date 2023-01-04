class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hashmap = {}
        
        for word in strs:
            word_list = list(word)
            word_list.sort()
            key = ''.join(word_list)
            
            if key in hashmap:
                hashmap[key] = hashmap[key] + [word]
            else:
                hashmap[key] = [word]
        
        return hashmap.values()