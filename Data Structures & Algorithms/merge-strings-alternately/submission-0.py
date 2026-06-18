class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        if len(word1) >= len(word2):
            word = word1
        else:
            word=word2

        p1=0
        p2=0
        res=""
        while p1 < len(word) or p2 < len(word):
            if p1 < len(word1):
                res += word1[p1]
            if p2 < len(word2):
                res += word2[p2]

            p1 += 1
            p2 += 1

        return res



        