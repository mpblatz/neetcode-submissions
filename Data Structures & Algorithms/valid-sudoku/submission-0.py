class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colMem = [[] for _ in range(9)]
        subBoxMem = [[] for _ in range(9)]
        for r in range(len(board)):
            rowMem = []
            for c in range(len(board[r])):
                n = board[r][c]
                if n == ".":
                    continue
                if n in rowMem:
                    return False
                elif n in colMem[c]:
                    return False

                sb = 0
                if r < 3:
                    if c >= 3 and c < 6:
                        sb = 1
                    elif c >= 6:
                        sb = 2
                elif r >= 3 and r < 6:
                    if c < 3:
                        sb = 3
                    elif c >= 3 and c < 6:
                        sb = 4
                    elif c >= 6:
                        sb = 5
                elif r >= 6:
                    if c < 3:
                        sb = 6
                    elif c >= 3 and c < 6:
                        sb = 7
                    elif c >= 6:
                        sb = 8
                if n in subBoxMem[sb]:
                    return False
                
                rowMem.append(n)
                colMem[c].append(n)
                subBoxMem[sb].append(n)
        return True