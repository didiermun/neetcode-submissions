class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        town judge has n-1 people who trust them and they do not trust themselves

        person 1, [2,3,4]

        indegree = [0]*n

        loop over the trust a b:
            graph[b].append(a)
            indegree[a] += 1

        trusted_by_n_1 = [i for i in graph where len(graph[i]) == n - 1]

        for person in trust_....:
            if person not in graph[person] and indegreee[person] == 0:
                return person

        return -1

        """

        if len(trust) == 0 and n == 1:
            return 1

        indegree = [0] * n
        graph = defaultdict(set)

        for a,b in trust:
            graph[b].add(a)
            indegree[a - 1] += 1

        trusted_by_all_but_self = [i for i in graph if len(graph[i]) == n - 1]

        for person in trusted_by_all_but_self:
            if person not in graph[person] and indegree[person - 1] == 0:
                return person

        return -1




        