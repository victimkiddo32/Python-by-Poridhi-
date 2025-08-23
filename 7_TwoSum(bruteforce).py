def two_sum(nums,target):
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []

# n=int(input())
nums=list(map(int,input().split()))
target=int(input())
result=two_sum(nums,target)
print(result)    