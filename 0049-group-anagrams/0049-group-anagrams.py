class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        anagram={}
        for i in range(n):
            word=sorted(strs[i])
            word="".join(word)
            if anagram.get(word):
                anagram[word].append(strs[i])
            else:
                anagram[word]=[strs[i]]
        
        ans=[]
        for value in anagram.values():
            ans.append(value)
        return ans