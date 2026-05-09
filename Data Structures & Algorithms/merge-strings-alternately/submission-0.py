class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # word1 = "abc" [0,1,2]
        # word2 = "xyz" [0,1,2]
        counter_w1 = 0
        counter_w2 = 0
        output = ""
        while counter_w1 < len(word1) and counter_w2 < len(word2):
            output += word1[counter_w1]
            output += word2[counter_w2]
            counter_w1 += 1
            counter_w2 += 1
        output += word1[counter_w1:]
        output += word2[counter_w2:]
        return output