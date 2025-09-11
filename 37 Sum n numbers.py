def Sum(n:int):
    if n==1:
        return 1
    return n + Sum(n-1)
    
    
#main code
def main():
    print(Sum(5))
    
main()    