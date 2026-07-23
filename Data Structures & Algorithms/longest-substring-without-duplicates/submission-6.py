class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # approach: iterate through the string s with a pointer r
        # make a window string, check while r is in the window that means theres a duplicate
        # keep shifting the left pointer up until the duplicate is gone
        # from there add the next right character, update max
        # return max count 
        
        max_count = 0
        l = 0
        window = set()

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1

            window.add(s[r])
            max_count = max(max_count, len(window))

        return max_count


        