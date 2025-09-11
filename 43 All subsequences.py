def allsubsequences(i:int ,nums:int,result=[]):
    #using recursion
    if i==len(nums):
        print(result)
        return
    
    #include nums[i]
    curr=nums[i]
    result.append(curr)
    allsubsequences(i+1,nums,result)
    
    #exclude nums[i]
    result.pop()
    allsubsequences(i+1,nums,result)
    
#main code
nums=[1,2,3]
allsubsequences(0,nums)
print()

    
    