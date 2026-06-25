class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1

        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i],0) + 1

        return countS == countT
        