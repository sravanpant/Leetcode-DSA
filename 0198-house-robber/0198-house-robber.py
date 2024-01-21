class Solution:
    def rob(self, nums: List[int]) -> int:
        
        maxLoot2, maxLoot1 = 0,0
        
        for i in nums:
            maxLoot2, maxLoot1 = maxLoot1, max(maxLoot2 + i, maxLoot1)
        
        return maxLoot1