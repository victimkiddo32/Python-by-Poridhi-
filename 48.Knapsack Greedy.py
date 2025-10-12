if __name__ == "__main__":
    weight=[18,15,10]
    value=[25,24,15]
    capacity=20
    n=len(value)
    ans=0
    ratio=[]
    for i in range(n):
        ratio.append([value[i]/weight[i],weight[i]])


    ratio=sorted(ratio,reverse=True)

    for r,w in ratio:
        if w<=capacity:
            ans+=r*w
            capacity-=w
        else:
            ans+=r*capacity
            capacity=0
            break
        

    print(ans)




