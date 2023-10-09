class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n = len(jewels)
        m = len(stones)
        count = 0
        stones_dict = dict()
        for i in range(m):
            stones_dict[stones[i]] = stones_dict.get(stones[i], 0)+1
        for j in range(n):
            for key, value in stones_dict.items():
                if jewels[j] == key:
                    count+=value
        return count