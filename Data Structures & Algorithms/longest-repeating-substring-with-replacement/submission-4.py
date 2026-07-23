class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # approach: make a hashmap for occurances (key = letter, value = frequency?)
        # loop through the entire string s with index i
        # count the occurance of each character and build the hashmap (but this should only be within the size of the sliding window)
        # keep increasing the size of the window until the number of replacements needed exceeds k
        # number of replacements = length of window - frequency of most frequent character
        # when that happens while replacements > k remove that leftmost character from the window and increase L
        # once the window is valid again validate max = r-l+1

        freq = {} # key = character, value = freq
        l=0
        max_count = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1 
            # (r-l+1) = window size
            # window size - most freq character = replacement

            # Length: 5 ("AABAB")
            # freq is {A:3, B:2}, so max is 3
            # 5 - 3 = 2, the two B's, which are exactly what you'd have to change to make it all A's

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            max_count = max(max_count, r-l+1)

        return max_count







        