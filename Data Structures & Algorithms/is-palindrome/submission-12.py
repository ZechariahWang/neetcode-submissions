class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            # go from left side and clear all alpha nums
            while i < j and not s[i].isalnum():
                i += 1
            # go from right side and clear all alpha nums
            while j > i and not s[j].isalnum():
                j -=1
            # check if currnt char from l == current char from r
            if s[i].lower() != s[j].lower():
                return False
            # if it is increase l and ddecrease r, else return false
            i +=1
            j = j-1
        return True

            # "c".isalnum()

        # return true