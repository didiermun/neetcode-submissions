class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0]*numCourses
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course)

        q = deque([course for course in range(numCourses) if indegree[course] == 0])

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        if len(order) != numCourses:
            return []

        return order