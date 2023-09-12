class Solution:
    def secondHighest(self, s: str) -> int:
        s = list(s)
        s1 = set()
        for i in s:
            if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                i = int(i)
                s1.add(i)
        if len(s1) > 1:
            return sorted(list(s1))[-2]
        else:
            return -1