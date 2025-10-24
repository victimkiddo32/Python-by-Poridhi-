
#TC: o(n!)
#SC: o(n) cz of sets used
#board sc is o(n^2) but we are not using it for isSafe check here


class solution:
    def solveNQueens(self,n):
        res=[]
        board=[['.']*n for _ in range(n)]
        col_set=set()
        major_diagonal_set=set()
        minor_diagonal_set=set()

        def backtrack(row):
            if row==n:
                solution = ["".join(r) for r in board]   # Convert 2D board into string list
                res.append(solution)
                return 
            
            for col in range(n):
                if col in col_set or (row-col) in major_diagonal_set or (row+col) in minor_diagonal_set:
                    continue

                board[row][col]='Q'
                col_set.add(col)
                major_diagonal_set.add(row-col)
                minor_diagonal_set.add(row+col)

                backtrack(row+1)

                board[row][col]='.'
                col_set.remove(col)
                major_diagonal_set.remove(row-col)
                minor_diagonal_set.remove(row+col)

        backtrack(0)
        return res
        
if __name__=="__main__":
    n=4
    sol=solution()
    print(sol.solveNQueens(n))

#output: [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
