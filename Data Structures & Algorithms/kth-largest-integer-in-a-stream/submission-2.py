class KthLargest:
    # approach: use a min heap, max size of the min heap is k
    # that means that the first element is always gonna be the cap
    # for init, declare the min heap and also the k constant, ensure the min heap is only the size of k
    # for add, insert the element into the minheap, update it to be within the bounds, and then return the first element
    # Init Time complexity: O(n), Space Complexity O(k)
    # Add Time Complexity: O(logk), Space Complexity O(k)

    def __init__(self, k: int, nums: List[int]):
        self.minheap = list(nums)
        heapq.heapify(self.minheap)
        self.k = k

        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)