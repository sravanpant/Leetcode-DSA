class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for i in s:
            s1.append(s.index(i))
        for j in t:
            t1.append(t.index(j))
        if s1 == t1:
            return True
        return False
            