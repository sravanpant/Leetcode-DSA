class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minP=prices[0]
        ans=0
        for i in range(1, n):
            minP=min(minP, prices[i])
            ans=max(ans, prices[i]-minP)
        return ans