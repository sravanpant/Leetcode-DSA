class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            num = i
            count = 0
            while (num!=0):
                if (num&1):
                    count += 1
                num = num >> 1
            output.append(count)
        return output
        