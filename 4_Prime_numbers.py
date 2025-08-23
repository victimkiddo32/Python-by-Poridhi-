def prime_num(n):
    root=int(n**0.5)
    cnt=0
    for i in range(1,root+1):
        if(n%i==0):
            cnt+=1
            if( i !=n//i):
                cnt+=1
    return cnt==2

n=int(input())
print(prime_num(n))