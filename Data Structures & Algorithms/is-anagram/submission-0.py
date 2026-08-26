class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for char in s:
            s_dict[char] += 1

        for char in t:
            t_dict[char] += 1

        if len(s_dict) != len(t_dict):
            return False

        for key, value in s_dict.items():
            if t_dict[key] != value:
                return False

        return True