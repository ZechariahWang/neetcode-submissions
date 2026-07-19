class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
            
        return list(res.values())

        # approach:
        # make a dictionary to store all the lists of the grouped anagrams
        # loop through every string inside strs
        # loop through evert char in string
        # make a count var = [0] * 26
        # the key part: ascii a is alwas the same, same with ascii of every char
            # get the difference in the ascii values (a=97, z=122), this will be the key of the dict give us a value between 0-26
        """
        res = {}

        word = "aab"
        count = [
            0 : 2
            1 : 1
            2 : 0
            3 : 0
            ...
            26: 0
        ]
        """
            # after done looping, add count to res
        # at the very end, just return res