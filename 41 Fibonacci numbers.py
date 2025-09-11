def fib(n:int):
    if n==0 or n==1:
        return n
    return fib(n-2)+fib(n-1)
    

def main():
    n = 30
    series = [fib(i) for i in range(n + 1)]
    print(series)
    #just get the nth number
    print()
    print(fib(n))
    
main()    