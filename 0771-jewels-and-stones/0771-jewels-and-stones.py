class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n = len(jewels)
        m = len(stones)
        count = 0
        for i in range(n):
            for j in range(m):
                if jewels[i] == stones[j]:
                    count+=1
        return count