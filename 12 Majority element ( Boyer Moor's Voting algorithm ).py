def majority_element(nums):
    count =0
    cnadidate=0;
    for i in nums:
        if count==0:
            candidate=i
        if i==candidate:
            count+=1
        else:
            count-=1
    return candidate

nums=list(map(int,input().split()))
print(majority_element(nums))