class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_list = []
        zero_list = []
        for i in s:
            if i == "1":
                one_list.append(i)
            else:
                zero_list.append(i)
        if len(one_list) == 1:
            s1 = "".join(zero_list) + "".join(one_list)
        else:
            s1 = "".join(one_list[1:]) + "".join(zero_list) + one_list[0]
        return s1