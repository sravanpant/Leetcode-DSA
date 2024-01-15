class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        arr=[]
        while(i<j):
            ans = numbers[i]+numbers[j]
            if ans==target:
                i+=1
                j+=1
                arr.append(i)
                arr.append(j)
                break
            elif ans > target:
                j-=1
            else:
                i+=1
        return arr
        
            