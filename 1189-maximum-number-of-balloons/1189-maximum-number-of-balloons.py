class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n = len(text)
        balloon_dict = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for i in range(n):
            if text[i] in ["b", "a", "l", "o", "n"]:
                balloon_dict[text[i]] = balloon_dict.get(text[i])+1
        balloon_dict["l"] = balloon_dict.get("l")//2
        balloon_dict["o"] = balloon_dict.get("o")//2
        ans = min(balloon_dict["b"], balloon_dict["a"], balloon_dict["l"], balloon_dict["o"], balloon_dict["n"])
        return ans