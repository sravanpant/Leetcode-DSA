class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum = 0
        for i in range(n):
            binNum = bin(i)[2:]
            count = 0
            for c in binNum:
                if c == "1":
                    count += 1
            if count == k:
                sum += nums[i]
        return sum