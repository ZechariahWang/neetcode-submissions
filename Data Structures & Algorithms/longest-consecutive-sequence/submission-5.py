class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach: use a set, the reason is bc it removes duplicates from the list so we can check if there rlly is a consecutive sequence
        # loop through the set, check for the start of a sequence (if the current num -1 does not exist in the set, we know for sure this could potentially be the start of a sequence)
        # in the loop update a variable representing current sequence
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



                



                