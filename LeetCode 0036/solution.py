class Solution:
    def isValidSudoku(self, board):

        for i in range(9):

            row_hash = {}
            column_hash = {}
            sub_box_hash = {}
            for j in range(9):
                # row_hash
                if board[i][j] != "." and board[i][j] in row_hash:
                    return False
                if board[i][j] not in row_hash:
                    row_hash[board[i][j]] = 1

                # column_hash
                if board[j][i] != "." and board[j][i] in column_hash:
                    return False
                if board[j][i] not in column_hash:
                    column_hash[board[j][i]] = 1

                # sub_box_hash
                s_i = (i//3)*3 + j//3
                s_j = (i%3)*3 + j%3
                if board[s_i][s_j] != "." and board[s_i][s_j] in sub_box_hash:
                    return False
                if board[s_i][s_j] not in sub_box_hash:
                    sub_box_hash[board[s_i][s_j]] = 1
        
        return True

# Test Cases

s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))
board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))