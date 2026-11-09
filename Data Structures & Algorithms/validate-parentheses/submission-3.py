class Solution:
    def isValid(self, s: str) -> bool:
        tagPairs = {'{':'}', '(':')', '[':']'}
        openBrackets = []
        for b in s:
            if b in tagPairs:
                openBrackets.append(b)
            else:
                if not openBrackets:
                    return False
                if tagPairs[openBrackets.pop()] != b:
                    return False
        return not openBrackets



