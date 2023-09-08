from math import factorial

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            value = []
            for j in range(i + 1):
                value.append(factorial(i) // (factorial(j) * factorial(i - j)))
            output.append(value)
        return output

        
        