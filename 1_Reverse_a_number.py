def reverse(n):
    INT_MAX=2**31-1
    sign=-1 if n<0 else 1
    rev=0
    while n:
        digit=n%10
        if(rev>INT_MAX//10 or (rev==INT_MAX//10 and digit>7)):
            return 0
        rev=rev*10+digit
        n//=10
    return rev*sign
n=int(input())
print(reverse(n))

