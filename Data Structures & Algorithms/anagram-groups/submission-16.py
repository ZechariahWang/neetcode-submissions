class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # approach default dict, count list, append to res dict

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())
            

