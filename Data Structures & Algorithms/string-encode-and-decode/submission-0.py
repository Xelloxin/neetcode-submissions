from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            # Format: <length> + "#" + <string>
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find where the delimiter '#' is located
            j = i
            while s[j] != '#':
                j += 1
            
            # The substring between i and j is the integer length of the word
            length = int(s[i:j])
            
            # Extract the actual word using the length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Move index 'i' to the beginning of the next length indicator
            i = j + 1 + length
            
        return res
