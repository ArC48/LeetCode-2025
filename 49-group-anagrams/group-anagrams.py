class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = str(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        res = []
        for key in groups:
            res.append(groups[key])
        return res