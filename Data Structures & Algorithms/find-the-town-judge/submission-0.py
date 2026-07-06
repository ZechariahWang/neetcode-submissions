class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        candidates = []
        for i in range(len(trust)):
            candidates.append(trust[i][0])

        for i in range(n):
            if i+1 not in candidates:
                return i+1
        return -1



        