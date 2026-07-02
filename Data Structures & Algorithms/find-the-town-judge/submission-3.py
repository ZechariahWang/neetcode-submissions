class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusts_someone = [] # everyone in this list trusts someone else
        for i in range(len(trust)):
            trusts_someone.append(trust[i][0])

        trusted_by = {}
        for i in range(len(trust)):
            person = trust[i][1]
            trusted_by[person] = trusted_by.get(person, 0) + 1 # how many ppl trust this guy

        for i in range(n):
            person = i+1

            # condition 1: trusts nobody and condition 2: trusted by all others (aka n-1 sincce n is total num of ppl)
            if person not in trusts_someone and trusted_by.get(person, 0) == n - 1:
                return i+1

        return -1



        