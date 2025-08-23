def majority_element(nums):
    nums=sorted(nums)
    n=len(nums)
    mid=n//2
    return nums[mid]

nums=list(map(int,input().split()))
print(majority_element(nums))