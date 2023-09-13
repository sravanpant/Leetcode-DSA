class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = dict()
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0) + 1
            mp[t[i]] = mp.get(t[i], 0) - 1
        for i in mp:
            if mp[i] != 0:
                return False
        return True
        