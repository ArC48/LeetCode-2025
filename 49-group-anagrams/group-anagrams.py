class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            cs = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                cs[index] += 1
            cs = tuple(cs)
            if cs not in groups:
                groups[cs] = []
            groups[cs].append(word)
        
        res = []
        for key in groups:
            res.append(groups[key])
        return res
