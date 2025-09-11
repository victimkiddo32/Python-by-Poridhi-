#finding all prime numbers upto n using sieve of eratosthenes
def sieve_of_eratosthenes(n):
    is_prime=[True]*(n+1)
    is_prime[0]=is_prime[1]=False
    cnt=0
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j]=False
    for i in range(2,n+1):
        if(is_prime[i]):
            cnt+=1
            print(i,end=' ')
    print()
    print("Total prime numbers:")
    return cnt

n=int(input())
print(sieve_of_eratosthenes(n))