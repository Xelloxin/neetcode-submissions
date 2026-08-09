class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key = sorted letters, value = list of matching words
        anagrams = {}

        for word in strs:
            anagrams.setdefault("".join(sorted(word)), []).append(word)
        
        return list(anagrams.values())
