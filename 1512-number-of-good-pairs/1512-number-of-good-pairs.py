class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count_dict = {}
        count = 0
        for i in range(n):
            count_dict[nums[i]] = count_dict.get(nums[i], 0) + 1
        for j in count_dict.values():
            count += j*(j-1)//2
        return count