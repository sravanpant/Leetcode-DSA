class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        n = len(nums)
        num_int = set()
        for i in range(n):
            for j in range(nums[i][0], nums[i][-1] + 1):
                num_int.add(j)
        return len(num_int)
            
            
        