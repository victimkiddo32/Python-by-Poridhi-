#finds the majority element in an array using a dictionary
def majority_element(nums):
    counts={}
    for i in nums:
        counts[i] = 0 
    for i in nums:
        counts[i]+=1
        if counts[i]>len(nums)//2:
            return i
    return 0

nums=list(map(int,input().split()))
print(majority_element(nums))