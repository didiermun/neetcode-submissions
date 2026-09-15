class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for course, preq in prerequisites:
            indegree[course] += 1
            adj[preq].append(course)


        count = 0
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while q:
            count += 1
            course = q.popleft()
            for next_course in adj[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        return numCourses == count
        