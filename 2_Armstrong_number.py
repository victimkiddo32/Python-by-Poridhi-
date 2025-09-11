def armstrong(n):
    given=abs(n)
    m=n
    sum=0
    digit_count=0
    while n:
        digit_count+=1
        n//=10
    
    while m:
        digits=m%10
        sum+=digits**digit_count
        m//=10
    return sum==given
            
n=int(input())
if armstrong(n):
    print("Armstrong")        
else:print("Not Armstrong")