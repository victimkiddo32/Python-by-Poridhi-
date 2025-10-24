class solution:
    def permute(self,nums):
        res=[]
        def backtrack(start=0):
            if start==len(nums)-1:
                res.append(nums[:])
                return 
            
            for i in range(start,len(nums)):
                nums[start],nums[i]=nums[i],nums[start]
                backtrack(start+1)
                nums[start],nums[i]=nums[i],nums[start]

        backtrack()
        return res
    
if __name__=="__main__":
    nums=[1,2,3]
    sol=solution()
    print(sol.permute(nums))



                