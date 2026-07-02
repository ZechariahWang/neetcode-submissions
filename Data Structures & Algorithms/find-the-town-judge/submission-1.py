class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        candidates = []
        for i in range(len(trust)):
            candidates.append(trust[i][0])

        trusted_by = {}
        for i in range(len(trust)):
            trusted_by[trust[i][1]] = trusted_by.get(trust[i][1], 0) + 1

        for i in range(n):
            if i + 1 not in candidates and trusted_by.get(i + 1, 0) == n - 1:
                return i+1
        return -1



        