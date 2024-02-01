class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,0
        while r<n:
            count=1
            while r+1<n and nums[r] == nums[r+1]:
                r+=1
                count+=1
            
            for i in range(min(2,count)):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l