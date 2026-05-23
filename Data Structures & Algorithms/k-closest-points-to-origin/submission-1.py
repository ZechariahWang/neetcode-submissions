class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
    
        for i in range(len(points)):
            point = points[i]
            error = math.sqrt((point[0]-0)**2 + (point[1]-0)**2)
            heapq.heappush(maxHeap, (-error, point[0], point[1]))
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [[x,y] for [_, x, y] in maxHeap]



        