#git add . ; git commit -m "Dp problem" ; git push -u origin main

#tabulation appraoch 0/1 knapsack
#TC: o(n*capacity)
#SC: 0(capacity)

def f(n,capacity,weight,value):
    prev=[0]*(capacity+1)
    for c in range(capacity+1):
        if weight[0]<=c:
            prev[c]=value[0]

    for i in range(1,n):
        curr=[0]*(capacity+1)
        for c in range(capacity+1):
            not_take=prev[c]
            take=-1
            if weight[i]<=c:
                take=value[i]+prev[c-weight[i]]
        curr[c]=max(take,not_take)
        prev=curr

    return prev[capacity]

     
if __name__=="__main__":
    weight=[3,2,5]
    value=[30,40,60]
    capacity=6
    n=len(value)
    ans=f(n-1,capacity,weight,value)
    print(ans)






