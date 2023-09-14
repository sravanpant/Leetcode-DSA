class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        greatest = [-1]
        maximum = arr[n-1]
        for i in range(n-2, -1, -1):
                maximum = max(arr[i+1], maximum)
                greatest.append(maximum)
        return greatest[::-1]
                    
                
        