class Solution:
    # approach: encode
    # encode in the format 3#sun
    # decode:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j+1
            res.append(s[i:i+length])
            i += length

        return res
