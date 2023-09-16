import sys
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        i = 0
        j = k-1
        n = len(nums)
        ans = float("inf")
        while(j<n):
            diff = nums[j]-nums[i]
            ans = min(ans,diff)
            i+=1
            j+=1
        
        return ans