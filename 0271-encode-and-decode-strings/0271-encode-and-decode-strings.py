class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for string in strs:
            n = len(string)
            encoded_string += str(n) + '#' + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        idx = 0
        while idx < len(s):
            n = ""
            while s[idx] != "#":
                n = n + s[idx]
                idx += 1
            idx += 1 
            end = idx + int(n)
            strs.append(s[idx:end])
            idx = end
        return strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))