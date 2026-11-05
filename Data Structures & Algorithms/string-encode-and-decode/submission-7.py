class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = str(len(strs)) + "~"
        for i in range(len(strs)):
            encoded_string += strs[i]
            if i < len(strs) - 1:
                encoded_string += "~"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("~")
        print(decoded_strs)
        if decoded_strs[0] == '0':
            return []
        return decoded_strs[1:]
