import copy

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def valid(board, row, col):
            n = len(board)

            for i in range(len(board)):
                if board[i][col] == "Q":
                    return False

            #左上
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False

                i = i - 1
                j = j - 1

            #右下
            i = row + 1
            j = col + 1
            while i < n and j < n:
                if board[i][j] == "Q":
                    return False

                i = i + 1
                j = j + 1

            #右上
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False

                i = i - 1
                j = j + 1

            #左下
            i = row + 1
            j = col - 1
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False

                i = i + 1
                j = j - 1

            return True

        def backtrace(board, row):
            if row == len(board):
                result.append(copy.deepcopy(board))
                return

            col_n = len(board[row])

            for col in range(col_n):
                if not valid(board, row, col):
                    continue

                board[row][col] = "Q"
                backtrace(board, row + 1)
                board[row][col] = "."

        result = []

        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(".")
            board.append(row)

        backtrace(board, 0)

        return result

slt = Solution()
print(slt.solveNQueens(4))