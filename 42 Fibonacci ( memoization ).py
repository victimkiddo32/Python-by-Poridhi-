memo={0:0,1:1}  
def fib(n:int):
    if n in memo:
        return memo[n]
    res=fib(n-1)+fib(n-2)
    memo[n]=res
    return res
    

def main():
    print(fib(30))
    
main()