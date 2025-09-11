from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(i:int,curr:List[int]):
            if i==len(nums):
                result.append(curr.copy())
                return
            
            #include nums[i]
            curr.append(nums[i])
            backtrack(i+1,curr)
            #exclude nums[i]
            curr.pop()
            backtrack(i+1,curr)
            
        backtrack(0,[])
        return result
    
#main code
nums=[1,2,3]
sol=Solution()
print(sol.subsets(nums))