class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # start with two pointers, one at 0 and the other also at 0
        # each time u move pointer, insert into a set
        # i stays in place, j keeps moving up while current char is not in the set
        # if j is in the set, keep moving i up and removing that item from the set until its not in there anymore
        # then keep moving j up
        # at each step, update the max size of the set
        # at the end, return the max length of the set

        max_length = 0
        window = set()

        i = 0
        for j in range(len(s)):
            while s[j] in window:
                window.remove(s[i])
                i += 1
                max_length = max(len(window), max_length)
            
            window.add(s[j])
            max_length = max(len(window), max_length)

        return max_length





        