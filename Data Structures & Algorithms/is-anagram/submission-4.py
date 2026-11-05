class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        sSort = "".join(sorted(s))
        tSort = "".join(sorted(t))
        return sSort == tSort
        