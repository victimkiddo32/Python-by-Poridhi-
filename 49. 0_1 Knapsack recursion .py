def f(i,capacity,w,v):
    if i==0:
        if w[0]<=capacity:
            return v[0]
        else:
            return 0
    not_take=f(i-1,capacity,w,v)
    take=-1
    if w[i]<=capacity:
        take=v[i]+f(i-1,capacity-w[i],w,v)
    
    return max(take,not_take)



#0/1 kanpsack using recursion

if __name__ == "__main__":
    weight=[3,2,5]
    value=[30,40,60]
    capacity=6
    n=len(value)
    ans=f(n-1,capacity,weight,value)
    print(ans)





