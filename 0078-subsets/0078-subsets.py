class Solution:
    def solve(self, idx, seq, subseq, nums, n):
        if idx == n:
            seq.append(subseq[:])
            return

        subseq.append(nums[idx])
        self.solve(idx + 1, seq, subseq[:], nums, n)
        subseq.pop()
        self.solve(idx + 1, seq, subseq[:], nums, n)
        return
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subseq = []
        seq = []
        n = len(nums)
        self.solve(0, seq, subseq, nums, n)
        return seq
        
        