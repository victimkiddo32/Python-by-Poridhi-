#git add . ; git commit -m "Dp problem" ; git push -u origin main

#Tabulation approach
#TC: O(n)
#SC: O(n)

def f(s, n):
    if n==0:
        return 1
    if s[0]=="0":
        return 0
    #cause 06 is not valid
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,n+1):
        #take i digit
        one_digit=0
        if s[i-1]!='0':
            one_digit=dp[i-1]
        two_digit=0
        #take 2 digit
        if i>=2 and 10<=int(s[i-2:i])<=26:
            two_digit=dp[i-2]

        dp[i]=one_digit+two_digit

    return dp[n]

#dp array for 226 is [1,1,2,3]

# dp array for 10 is [1,1,1]

if __name__ == "__main__":
    s = input("Enter a numeric string: ")
    n = len(s)
    ans = f(s,n)
    print("Number of possible decodings:", ans)
