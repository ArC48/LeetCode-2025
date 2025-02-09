class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for word in strs:
            key = hash(str(sorted(word)))
            if key in mapping:
                mapping[key].append(word)
            else:
                mapping[key] = [word]
        
        result = []
        for key in mapping:
            result.append(mapping[key])
        
        return result