def findDuplicate(nums):
    slow=nums[0]
    fast=nums[0]
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break
    
    slow=nums[0]
    while slow is not fast:
        slow=nums[slow]
        fast=nums[fast]
        
    return slow
        
    
#Main code
nums = [1, 3, 4, 3, 2]
print(findDuplicate(nums)) 