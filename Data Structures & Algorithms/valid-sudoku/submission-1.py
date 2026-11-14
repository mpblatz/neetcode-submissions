class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        currCols = [set() for _ in range(len(board))]
        currBoxes = [set() for _ in range(len(board))]
        for row in range(len(board)):
            currRow = set()
            for col in range(len(board[row])):
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell in currRow or cell in currCols[col]:
                    return False
                else:
                    currRow.add(cell)
                    currCols[col].add(cell)
                if row <= 2:
                    if col <= 2:
                        if cell in currBoxes[1]:
                            return False
                        else:
                            currBoxes[1].add(cell)
                    if col > 2 and col <= 5:
                        if cell in currBoxes[2]:
                            return False
                        else:
                            currBoxes[2].add(cell)
                    if col > 5:
                        if cell in currBoxes[3]:
                            return False
                        else:
                            currBoxes[3].add(cell)
                if row > 2 and row <= 5:
                    if col <= 2:
                        if cell in currBoxes[4]:
                            return False
                        else:
                            currBoxes[4].add(cell)
                    if col > 2 and col <= 5:
                        if cell in currBoxes[5]:
                            return False
                        else:
                            currBoxes[5].add(cell)
                    if col > 5:
                        if cell in currBoxes[6]:
                            return False
                        else:
                            currBoxes[6].add(cell)
                if row > 5:
                    if col <= 2:
                        if cell in currBoxes[7]:
                            return False
                        else:
                            currBoxes[7].add(cell)
                    if col > 2 and col <= 5:
                        if cell in currBoxes[8]:
                            return False
                        else:
                            currBoxes[8].add(cell)
                    if col > 5:
                        if cell in currBoxes[0]:
                            return False
                        else:
                            currBoxes[0].add(cell)
        return True