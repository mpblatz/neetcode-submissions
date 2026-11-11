class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        ags = {}
        for s in strs:
            skey = "".join(sorted(s))
            if skey not in ags:
                ags[skey] = []
            ags[skey].append(s)
        return list(ags.values())