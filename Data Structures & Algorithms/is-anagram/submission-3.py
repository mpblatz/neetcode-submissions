class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h = {}
        for i in range(len(s)):
            h[s[i]] = h.get(s[i], 0) + 1
            h[t[i]] = h.get(t[i], 0) - 1
        
        for v in h.values():
            if v != 0:
                return False
        return True