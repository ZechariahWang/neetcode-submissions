class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach: check the number PRIOR to each
        # convert nums into a set to avoid duplicates and make sure we get numbers in O(1) time
        # if n-1 is NOT in nums, then that meeans that there is a chance that this is the start of a potential sequence
        # keep iterating while n+1 exists inside the set, while also updpateing a max_seq var
        # at the very end, r eturn max_seq

        max_seq = 0
        num_set = set(nums)

        for n in num_set:
            if n-1 not in num_set:
                seq = 1
                while n+seq in num_set:
                    seq += 1
                max_seq = max(max_seq, seq)
        
        return max_seq

        