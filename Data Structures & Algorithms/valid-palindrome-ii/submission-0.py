class Solution:

    def isPalindrome(self, s: str):
        l, r = 0, len(s)-1
        while l <= r :
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l]!=s[r]:
                return False
            l += 1
            r -= 1

        return True


    def validPalindrome(self, s: str) -> bool:

        isInitialPalindrome = self.isPalindrome(s)
        if isInitialPalindrome:
            return True
        else:
            for i in range(len(s)):
                test_string = s
                test_string = test_string.replace(s[i], "")

                isPalindrome = self.isPalindrome(test_string)
                if isPalindrome:
                    return True

        return False



        