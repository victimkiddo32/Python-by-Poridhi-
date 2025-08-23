def maxprofit(prices):
    n=len(prices)
    if n==0:
        return 0
    min_price=prices[0]
    maxprofit=0
    for i in range(1,n):
        if prices[i]<min_price:
            min_price=prices[i]
        elif prices[i]-min_price>maxprofit:
            maxprofit=prices[i]-min_price
    return maxprofit

prices=list(map(int,input().split()))
result=maxprofit(prices)
print(result)

