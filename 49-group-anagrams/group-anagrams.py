class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for word in strs:
            curr_map = [0] * 26

            for ch in word:
                curr_map[ord(ch) - ord("a")] += 1

            if tuple(curr_map) in mapping:
                mapping[tuple(curr_map)].append(word)
            else:
                mapping[tuple(curr_map)] = [word]
        
        result = []
        for key in mapping:
            result.append(mapping[key])
        
        return result