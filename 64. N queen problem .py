#git add . ; git commit -m "Backtracking" ; git push -u origin main

#TC: o(n!)
#SC: o(n^2)

class Solution:
    def solveNQueens(self,n):
        res=[]
        board=[['.']*n for _ in range(n)]

        def isSafe(row,col):
            for i in range(n):
                for j in range(n):
                    if board[i][j]=='Q':
                        if j==col or i+j==row+col or i-j==row-col:
                            return False
            return True
        
        def backtrack(row,positions):
            if row==n:
                res.append(positions[:])
                return

            for col in range(n):
                if isSafe(row,col):
                    board[row][col]='Q'
                    positions.append(col+1)
                    backtrack(row+1,positions)
                    positions.pop()
                    board[row][col]='.'

        backtrack(0,[])
        return res
    
if __name__=="__main__":
    n=4
    sol=Solution()
    print(sol.solveNQueens(n))

#output: [[2, 4, 1, 3], [3, 1, 4, 2]]







