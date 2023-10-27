class Solution:
    def solve(self, seq, subseq, nums, idx, n):
        if idx == n:
            seq.append(subseq[:])
            return
        subseq.append(nums[idx])
        self.solve(seq, subseq[:],nums, idx+1, n)
        subseq.pop()
        self.solve(seq, subseq[:], nums, idx+1, n)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seq = []
        subseq = []
        n = len(nums)
        idx = 0
        self.solve(seq, subseq, nums, idx, n)
        return seq