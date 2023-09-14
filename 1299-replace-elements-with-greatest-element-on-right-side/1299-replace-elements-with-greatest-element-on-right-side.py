class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maximum = arr[n-1]
        arr[n-1] = -1
        for i in range(n-2, -1, -1):
            temp = arr[i]
            arr[i] = maximum
            maximum = max(maximum, temp)
        return arr
                    
                
        