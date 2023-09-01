class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            count = 0
            i = bin(i)[2:]
            for j in i:
                if j == "1":
                    count += 1
            output.append(count)
        return output
        