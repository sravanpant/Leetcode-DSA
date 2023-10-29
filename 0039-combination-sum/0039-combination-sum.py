class Solution:
    def solve(self, seq, subseq, nums, idx, target, n):
        if idx == n:
            if target == 0:
                seq.append(subseq[:])
            return
                
        if target >= nums[idx]:
            subseq.append(nums[idx])
            self.solve(seq, subseq, nums,idx, target - nums[idx], n)
            subseq.pop()
        self.solve(seq, subseq, nums, idx+1, target, n)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        seq = []
        subseq = []
        idx = 0
        n = len(candidates)
        self.solve(seq, subseq, candidates, idx, target, n)
        return seq