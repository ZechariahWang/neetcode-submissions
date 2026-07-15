class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in range(len(strs)):
            res.append(str(len(strs[i])))
            res.append("#")
            res.append(strs[i])
        print(res)
        print("".join(res))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


        
