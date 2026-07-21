class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach: use a set, the reason is bc it removes duplicates from the list so we can check if there rlly is a consecutive sequence
        # loop through the set, check for the start of a sequence (if the current num -1 does not exist in the set, we know for sure this could potentially be the start of a sequence)
        # in the loop make a variable representing length, and one representing the current number
        # do a while loop, check while current+1 is in num_set, we know we can def continue the sequence
        # update current and length by 1
        # outside the loop, once the sequence has run its course, check to see if it was longer than our global longest so far, if it is update it
        # return longest
        longest=0
        num_set = set(nums)
        for n in num_set:
            if n-1 not in num_set:
                length=1
                current=n
                while current+1 in num_set:
                    length+=1
                    current+=1

                if length > longest:
                    longest = length

        return longest



                



                