class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(len(board)):
            row = set()
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row:
                    return False
                row.add(num)

        # check columns
        for i in range(len(board)):
            col = set()
            for j in range(len(board)):
                num = board[j][i]
                if num == ".":
                    continue
                if num in col:
                    return False
                col.add(num)

        # check 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = set()
                for row in range(3):
                    for col in range(3):
                        num = board[i + row][j + col]
                        if num == ".":
                            continue
                        if num in box:
                            return False
                        box.add(num)
        
        return True
            