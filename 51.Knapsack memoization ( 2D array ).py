#git add . ; git commit -m "Dp problem" ; git push -u origin main


#memoization of 0/1 knapsack
#TC: o(n*capacity)
#SC: o(n*capcity) + o(n) for recursion stack
 
def f(i,capacity,w,v,memo):
    if i<0 or capacity==0:
        return 0
    if memo[i][capacity]!=-1:
        return memo[i][capacity]
    not_take=f(i-1,capacity,w,v,memo)
    take=-1
    if w[i]<=capacity:
        take=v[i]+f(i-1,capacity-w[i],w,v,memo)
    
    memo[i][capacity]=max(take,not_take)
    return memo[i][capacity]

if __name__ == "__main__":
    weight=[3,2,5]
    value=[30,40,60]
    capacity=6
    n=len(value)
    memo=[[-1]*(capacity+1) for w in range(n)]
    ans=f(n-1,capacity,weight,value,memo)
    print(ans)
