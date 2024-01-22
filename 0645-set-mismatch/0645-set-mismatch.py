class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        n = len(nums)
        dup, missing = -1, -1

        for i in range(1, n + 1):
            count = nums.count(i)
            if count == 2:
                dup = i
            elif count == 0:
                missing = i

        return [dup, missing]