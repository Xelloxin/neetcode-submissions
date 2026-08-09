from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Create an array of 26 zeros for character counts
            count = [0] * 26
            
            # Count the frequency of each character in the word
            for char in word:
                # ord() gets the ASCII value. ord('a') is 97.
                # So ord('b') - ord('a') gives index 1.
                count[ord(char) - ord('a')] += 1
                
            # Tuples can be used as dictionary keys, lists cannot
            signature = tuple(count)
            anagram_map[signature].append(word)
            
        return list(anagram_map.values())
