class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # approach: iterate through the string s for each index i
        # check how long it takes until it reaches a character not equal to s[i]
        max_count=0

        if len(s) == 0:
            return 0

        for i in range(len(s)):
            count=0
            current_string = ""
            for j in range(i, len(s)):
                if s[j] not in current_string:
                    current_string += s[j]
                    count += 1
                else: # need this so that when string is automatically found invalid, break out 
                    break
            max_count = max(max_count, count)

        return max_count

        