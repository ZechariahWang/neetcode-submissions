# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        current_guess=0

        while l <= r:
            m = (l + r)//2
            current_guess = guess(m)
            if current_guess == 0:
                return m # returnt the num, not the guess val call from API
            if current_guess == -1: # m > target
                r = m - 1
            if current_guess == 1: # m < target
                l = m + 1

        return current_guess
