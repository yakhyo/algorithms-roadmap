class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate_row(rows):
            for row in rows:
                seen = set()
                for ch in row:
                    if ch != ".":
                        if ch in seen:
                            return False
                        seen.add(ch)
            return True

        def validate_col(rows):
            for i in range(len(rows)):
                seen = set()
                for j in range(len(rows[0])):
                    if rows[j][i] != ".":
                        if rows[j][i] in seen:
                            return False
                        seen.add(rows[j][i])
            return True

        def validate_square(rows):
            for row_start in [0, 3, 6]:
                for col_start in [0, 3, 6]:
                    seen = set()
                    for i in range(3):
                        for j in range(3):
                            ind_i = row_start + i
                            ind_j = col_start + j
                            if rows[ind_i][ind_j] != ".":
                                if rows[ind_i][ind_j] in seen:
                                    return False
                                seen.add(rows[ind_i][ind_j])
            return True

        if validate_row(board) and validate_col(board) and validate_square(board):
            return True
        return False
