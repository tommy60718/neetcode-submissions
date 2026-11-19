class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We use dict(set) to store rows, columns, square. to check duplicates

        rows_check = collections.defaultdict(set) # 0~8 rows
        columns_check = collections.defaultdict(set) # 0 ~ 8 columns
        squares_check = collections.defaultdict(set) # [0][0] ~ [2][2] squares

        # Iterate through all 9 x 9 grids
        for r in range(9):
            for c in range(9):
                # Skip "."
                if board[r][c] == ".":
                    continue
                # check valid
                if (board[r][c] in rows_check[r] or
                    board[r][c] in columns_check[c] or
                    board[r][c] in squares_check[(r//3,c//3)]
                    ):
                    return False
                # update to dict
                rows_check[r].add(board[r][c])
                columns_check[c].add(board[r][c])
                squares_check[(r//3,c//3)].add(board[r][c])


        return True