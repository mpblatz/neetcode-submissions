class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSort = "".join(sorted(s))
        tSort = "".join(sorted(t))
        return sSort == tSort
        