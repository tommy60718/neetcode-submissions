class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize hash sets
        # Collections.defaultdict -> my_dict[1] += 1 or my_dict.get(1, 0) += 1
        # dict(int or tuple :set)
        rows_check = collections.defaultdict(set) # row 0 ~ 8
        columns_check = collections.defaultdict(set) # column 0 ~ 8
        squares_check = collections.defaultdict(set) # square[0][0] ~ square[2][2]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # check valid
                if (board[r][c] in rows_check[r] or
                    board[r][c] in columns_check[c] or
                    board[r][c] in squares_check[(r//3, c//3)]
                ):
                    return False
                # update dicts
                rows_check[r].add(board[r][c])
                columns_check[c].add(board[r][c])
                squares_check[(r//3,c//3)].add(board[r][c])
        return True