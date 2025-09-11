def GCD(x, y):
    while y != 0:
        x, y = y,x % y
    return x

x=int(input())
y=int(input())
print(GCD(x,y))
