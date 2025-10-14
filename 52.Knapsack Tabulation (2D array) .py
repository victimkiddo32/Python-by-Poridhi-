#git add . ; git commit -m "Dp problem" ; git push -u origin main

#tabulation appraoch 0/1 knapsack
#TC: o(n*capacity)
#SC: o(n*capcity)
def f(n,capacity,weight,value):
    dp=[[0]*(capacity+1) for _ in range(n)]
    for c in range(capacity+1):
        if weight[0]<=c:
            dp[0][c]=value[0]

    for i in range(1,n):
        for c in range(capacity+1):
            not_take=dp[i-1][c]
            take=-1
            if weight[i]<=c:
                take=value[i]+dp[i-1][c-weight[i]]

        dp[i][c]=max(take,not_take)
    
    return dp[n-1][capacity]

if __name__=="__main__":
    weight=[3,2,5]
    value=[30,40,60]
    capacity=6
    n=len(value)
    ans=f(n-1,capacity,weight,value)
    print(ans)






