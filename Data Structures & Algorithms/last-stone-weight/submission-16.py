class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # approach: use a max heap
        # use a min heap, but store all values as negative numbers, effectively turning it into a max heap
        # declare a max heap before the loop
        # loop until len max heap <= 1
        # pop the first two elements of the heap, x and y, reverse them so its x=-x,y= -y
        # if x == y, discard both of them
        # if x != y, y = x-y and destroy x, push -y into the heap
        # keep doing this until there is only one stone left
        # at the end return the 0 index of the heap, return that last element but negative otherwise just return 0
        # time complexity: O(nlogn), space complexity: O(n)
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                y = x -y
                heapq.heappush(heap, -y)
            
        return -heap[0] if len(heap) == 1 else 0

