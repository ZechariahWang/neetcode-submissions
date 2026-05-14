class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr=[]
        self.k=k
        for i in range(len(nums)):
            self.arr.append(nums[i])

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[-self.k]

        
