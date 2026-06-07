class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # strategy:
        # make a count dictionary for to count how many times a number appears
        # key = number, val = how many times that number appears
        # make a list of frequencies, each frequency is a list so basically index = how many times it appears
        # list = all the numbers that appear the amount of the time the index does (ex: 1: [4,3,2]) 4,3 2 all occur one time
        # frequency last index will host the largest element

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for c, n in count.items():
            freq[n].append(c)

        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                return freq[i][0]





        