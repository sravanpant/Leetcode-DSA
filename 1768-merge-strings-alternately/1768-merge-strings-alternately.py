class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i=0
        j=0
        word3 = ""
        while i<n and j<m:
            word3 = word3 + word1[i] + word2[j]
            i+=1
            j+=1
            
        while i<n:
            word3 = word3 + word1[i]
            i+=1
        
        while j<m:
            word3 = word3 + word2[j]
            j+=1
            
        return word3
    