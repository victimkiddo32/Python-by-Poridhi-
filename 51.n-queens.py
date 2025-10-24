#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List

#TC : o(n!)
#SC: o(n^2)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.']*n for _ in range(n)]

        def isSafe(row,col):
            for i in range(n):
                for j in range(n):
                    if board[i][j]=='Q':
                        if j==col or i+j==row+col or i-j==row-col:
                            return False
            return True
        
        def backtrack(row):
            if row==n:
                solution = ["".join(r) for r in board]   # Convert 2D board into string list
                res.append(solution)
                return

            for col in range(n):
                if isSafe(row,col):
                    board[row][col]='Q'
                    backtrack(row+1)
                    board[row][col]='.'

        backtrack(0)
        return res
        
# @lc code=end

if __name__=="__main__":
    n=4
    sol=Solution()
    print(sol.solveNQueens(n))

#output: [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
