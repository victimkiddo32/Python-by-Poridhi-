def f(i,capacity,w,v,r):
    if i < 0 or capacity <= 0:
        return 0
    
    value, weight = v[i], w[i]
    
    if weight <= capacity:
        # Take full item
        return value + f(i-1, capacity - weight, w, v, r)
    else:
        # Take fraction of item to fill remaining capacity
        return (value / weight) * capacity
    
    
    

#fractional kanpsack using recursion

if __name__ == "__main__":
    weight=[18,15,10]
    value=[25,24,15]
    capacity=20
    n=len(value)
    ratio=[]
    for i in range(n):
        ratio.append([value[i]/weight[i],weight[i]])


    ratio=sorted(ratio,reverse=True)

    ans=f(n-1,capacity,weight,value,ratio)
    print(ans)





