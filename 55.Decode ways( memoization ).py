#git add . ; git commit -m "Dp problem" ; git push -u origin main

#memoizarion approach
#TC: O(n)
#SC: o(n)+o(n) for recursion stack
def f(s, n,memo):
    if n == 0:
        return 1
    if s[0] == '0':
        return 0
    #cause 06 is not valid
    if (s,n) in memo:
        return memo[(s,n)]

    # take 1 digit
    one_digit = f(s[1:],n-1,memo)

    # take 2 digits (if valid)
    two_digit = 0
    if n >= 2 and 10 <= int(s[:2]) <= 26:#check if first two digts are valid
        two_digit = f(s[2:], n - 2,memo)

    memo[(s,n)]=one_digit+two_digit
    return memo[(s,n)]


if __name__ == "__main__":
    s = input("Enter a numeric string: ")
    n = len(s)
    memo={}
    ans = f(s,n,memo)
    print("Number of possible decodings:", ans)
