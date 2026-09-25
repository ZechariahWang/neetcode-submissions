class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count dict fornumber of times a number appears
        # freq list of lists for an inde with a freq and a value of lists with all numbers that occur that amount of times
        # run bucket sort, find the ones at the very end of the list


        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                if len(res) == k:
                    return res
                res.append(n)

        return res

        