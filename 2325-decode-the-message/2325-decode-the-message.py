class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        n = len(key)
        m = len(message)
        key_dict = {}
        num = 97
        for i in range(n):
            if key[i] not in key_dict:
                key_dict[key[i]] = chr(num)
                num += 1

        decoded_message = []
        for j in range(m):
            if message[j] == " ":
                decoded_message.append(" ")
            else:
                decoded_message.append(key_dict.get(message[j]))
        return "".join(decoded_message)
            