def sum_of_divisors(n):
    root=int(n**0.5)
    sum=0
    for i in range(1,root+1):
        if n%i==0:
            sum+=i
            if i !=n//i:
                sum+=n//i
    return sum
n=int(input())
print(sum_of_divisors(n))

#12 -> 1+2+3+4+6+12=28
