class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sWordCounts = {}
        tWordCounts = {}

        for charS, charT in zip(s, t):
            sWordCounts[charS] = sWordCounts.get(charS, 0) + 1
            tWordCounts[charT] = tWordCounts.get(charT, 0) + 1
        
        if len(sWordCounts) != len(tWordCounts):
            return False

        for char in sWordCounts:
            if char not in tWordCounts or tWordCounts[char] != sWordCounts[char]:
                return False
        return True
        
