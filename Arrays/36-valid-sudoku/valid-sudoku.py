class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Arrays to track seen numbers in rows,
        # columns, and sub-matrix
        rows = [0] * 9
        cols = [0] * 9
        subMat = [0] * 9

        for i in range(9):
            for j in range(9):
                # Skip empty cells
                if board[i][j] == '.':
                    continue

                val = int(board[i][j])
                pos = 1 << (val - 1)

                # Check for duplicates in the current row
                if (rows[i] & pos) > 0:
                    return False
                rows[i] |= pos

                # Check for duplicates in the current column
                if (cols[j] & pos) > 0:
                    return False
                cols[j] |= pos

                # Calculate the index for the 3x3 sub-matrix
                idx = (i // 3) * 3 + j // 3

                # Check for duplicates in the current sub-matrix
                if (subMat[idx] & pos) > 0:
                    return False
                subMat[idx] |= pos

        return True