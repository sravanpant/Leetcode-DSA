class Solution:
    def increment(self, s):
            if s == "z":
                return "a"
            ascii_value = ord(s)
            ascii_value += 1
            return chr(ascii_value)
        
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        while i<len(str1) and j<len(str2):
            if str1[i] == str2[j] or self.increment(str1[i]) == str2[j]:
                i+=1
                j+=1
            else:
                i+=1
        return j==len(str2)
        
        