class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) + 1
            counter[t[i]] = counter.get(t[i], 0) - 1

        return all(val == 0 for val in counter.values())
        