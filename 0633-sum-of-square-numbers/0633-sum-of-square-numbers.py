class Solution:
    
    
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j=int(sqrt(c))
        
        while i<=j:
            ans = i*i + j*j
            if ans<c:
                i+=1
            elif ans == c:
                return True
            else: 
                j-=1
                