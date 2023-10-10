class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n = len(text)
        balloon_dict = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for i in range(n):
            if text[i] in ["b", "a", "l", "o", "n"]:
                balloon_dict[text[i]] = balloon_dict.get(text[i])+1
        m = min(balloon_dict["l"], balloon_dict["o"]) // 2
        if balloon_dict["b"] >= m and balloon_dict["a"] >= m and balloon_dict["n"]>= m:
            return m
        elif (balloon_dict["l"] and balloon_dict["o"])>=2:
            ans = min(balloon_dict["b"], balloon_dict["a"], balloon_dict["n"])
            return ans
        return 0