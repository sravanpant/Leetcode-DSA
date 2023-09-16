class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        nums1 = sorted(nums)
        if nums == nums1:
            return 0
        n = len(nums)
        for j in range(n - 1):
            for i in range(n - 1, 0, -1):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            if nums == nums1:
                return j + 1
        return -1
        
        