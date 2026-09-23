class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # approach: run dfs, we are looking for a cycle
        # turn the prereq list into a graph
        # each node is a course which points to all courses you must take to take that course
        # if there is a loop somewhere, then it is not possible to finish, return false
        # otherwise, its possible to finish, return true
        #
        # convert the prereq list into a graph
        # the graph is in the form of a hashmap, where the key is the node and the value is a list of all nodes it connects to
        # make a path set, so that you can keep track of nodes already visited during traversal
        # through each dfs look, check if the node is in the path, if it is return true since theres a cycle 
        # add current node to the path
        # run a for loop through all nodes connected to current, and run dfs on them
        # remove current node from the path
        # outside dfs, run a for loop and run dfs from every single possible node, since you dont know where starting course is
        # if dfs returns true, then that means there is a cycle, return false
        # otherwise, return true

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        path = set()
        done = set()
        def dfs(course):
            if course in path:
                return True

            if course in done: # this has already been explored, definitely not a loop
                return False

            path.add(course)
            done.add(course)
            for item in graph[course]:
                if dfs(item):
                    return True

            path.remove(course)

        for i in range(numCourses):
            if dfs(i): # meaning there is a cycle
                return False
        return True






 
        
