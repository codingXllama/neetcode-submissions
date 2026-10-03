class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
           
        anagram_map = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord not in anagram_map:
                anagram_map[sortedWord] = [word]
                
            else:
                anagram_map[sortedWord].append(word)
        
        return list(anagram_map.values())