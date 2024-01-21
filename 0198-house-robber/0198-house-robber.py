class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return nums[0]
        
        maxLoot=[None]*n
        maxLoot[0]=nums[0]
        maxLoot[1]=max(nums[0], nums[1])
        
        for i in range(2,n):
            maxLoot[i]=max(maxLoot[i-2]+nums[i], maxLoot[i-1])
        
        return maxLoot[n-1]