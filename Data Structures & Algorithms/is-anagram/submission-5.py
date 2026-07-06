class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in set(s):
            if s.count(i) != t.count(i):
                return False

        return True

