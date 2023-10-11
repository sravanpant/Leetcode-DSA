class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum = 0
        totalSum = sum(nums)
        for i in range(n):
            if leftSum*2 + nums[i] == totalSum:
                return i
            else:
                leftSum += nums[i]
        return -1
                