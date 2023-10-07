class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n=len(nums)
        product=1
        for i in range(n):
            product *= nums[i]
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0