class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_dict = {}
        n = len(nums)
        for i in range(n):
            major_dict[nums[i]] = major_dict.get(nums[i], 0)+1
        for key, value in major_dict.items():
            if value > (n/2):
                return key