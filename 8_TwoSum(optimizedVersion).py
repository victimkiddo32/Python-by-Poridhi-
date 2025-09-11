#optimezed version using dictionary for o(n) time complexity
def two_sum(nums,target):
    n=len(nums)
    dict={}
    for i in range(n):
        complement=target-nums[i]
        if complement in dict:
            return [dict[complement],i]
        dict[nums[i]]=i
    return []

# n=int(input())
nums=list(map(int,input().split()))
target=int(input())
result=two_sum(nums,target)
print(result)    