def printNum(n:int):
    if n==0:
      return 0
    
    res=printNum(n-1)
    print(res)
    return n
    
    

#main code
def main():
    printNum(5)
    
main()    