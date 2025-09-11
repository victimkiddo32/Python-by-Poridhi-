def swap(x:int,y:int,nums:int):
    tmp=nums[x]
    nums[x]=nums[y]
    nums[y]=tmp
    
def reverse(nums:int):
    left=0
    right=len(nums)-1
    while left<right:
        swap(left,right,nums)
        left+=1
        right-=1
        
    
#main code
nums=list(map(int,input().split()))
reverse(nums)
print(nums)
    