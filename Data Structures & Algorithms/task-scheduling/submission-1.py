class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # make a hashmap to store the most frequent events
        # ex {x : 2, Y: 2}

        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        coolDown = deque()

        time = 0
        while maxHeap or coolDown:
            time += 1
            if maxHeap:
                c = heapq.heappop(maxHeap) + 1
                if c != 0:
                    coolDown.append((c, time+n))
            if coolDown and coolDown[0][1] == time:
                heapq.heappush(maxHeap, coolDown.popleft()[0])
        return time
            



        # process more frequent event first
        # start with largest event, then start the countdown. Then add in the second most frequent
        # event, etc. Once you start an event, assign it a counter of n that decrements by 1 each iteration
        # We can use a max heap for this, since the largest (aka the most frequent) event will appear first
        # once we cycle through that even, we pop it from the max heap and insert it into a queue
        # through each iteration, 
        