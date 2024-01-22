class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        countDict={}
        
        for i in range(1,n+1):
            countDict[i]=nums.count(i)
            
        ans=[]
        
        for key,value in countDict.items():
            if value==2:
                ans.append(key)
              
        for key, value in countDict.items():
            if value==0:
                ans.append(key)
                
        return ans