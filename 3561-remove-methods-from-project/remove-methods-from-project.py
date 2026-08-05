class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        incoming = [0] * n
        for u, v in invocations:
            graph[u].append(v)
            incoming[v] += 1
        queue = deque([k])
        suspicious = [False] * n
        suspicious[k] = True

        while queue:
            node = queue.popleft()

            for nxt in graph[node]:
                incoming[nxt] -= 1
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    queue.append(nxt)

        for i in range(n):
            if suspicious[i] and incoming[i] > 0:
                return list(range(n))

        remaining = []
        for i in range(n):
            if not suspicious[i]:
                remaining.append(i)
        return remaining