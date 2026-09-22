class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # approach: make graph, run dfs
        # trying to identify cycle in graph
        # if no cycle, then return true, can finish
        # else return false
        # run dfs starting from the first graph node, for each graph mark as visited
        # through each run check if graph is marked, if it is return false if its not keep going
        # graph = dict (key = desired course, val = need to take to qualify )

        graph = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        path = set()
        done = set()
        def dfs(course):
            if course in path:
                return True

            if course in done:
                return False

            path.add(course)
            done.add(course)
            for nxt in graph[course]:
                if dfs(nxt):
                    return True
            path.remove(course)
            return False

        for i in range(numCourses):
            if dfs(i):
                return False

        return True


 
        
