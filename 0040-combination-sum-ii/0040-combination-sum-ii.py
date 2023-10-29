class Solution:
    def solve(self, seq, subseq, nums, idx, target):
        n = len(nums)
        if target == 0:
            seq.append(subseq[:])
            return
        
        for i in range(idx, n):
            if i > idx and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                break
            subseq.append(nums[i])
            self.solve(seq, subseq, nums, i+1, target-nums[i])
            subseq.pop()
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        seq = []
        subseq = []
        self.solve(seq, subseq, candidates, 0, target)
        return seq