class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach 1
        # hashmap = {}
        # for word in strs:
        #     word_list = list(word)
        #     word_list.sort()
        #     key = ''.join(word_list)
        #     if key in hashmap:
        #         hashmap[key] = hashmap[key] + [word]
        #     else:
        #         hashmap[key] = [word]
        # return hashmap.values()
        
        # Approach 2
        hashmap = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
                
            key = tuple(count)
            if key in hashmap:
                hashmap[key] = hashmap[key] + [word]
            else:
                hashmap[key] = [word]
        return hashmap.values()
                