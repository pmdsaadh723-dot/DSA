class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_nodes = [(value, node) for node, value in enumerate(nums)]
        sorted_nodes.sort()
        position = {}
        for index, (_, node) in enumerate(sorted_nodes):
            position[node] = index
        farthest = [0] * n
        for index, (value, _) in enumerate(sorted_nodes):
            last = bisect_left(sorted_nodes, (value + maxDiff, inf)) - 1
            farthest[index] = last
        LOG = n.bit_length()
        jump = [farthest]
        for _ in range(1, LOG):
            previous = jump[-1]
            jump.append([previous[previous[i]] for i in range(n)])
        answer = []
        for start, end in queries:
            left = position[start]
            right = position[end]
            if left == right:
                answer.append(0)
                continue
            if left > right:
                left, right = right, left
            current = left
            distance = 0
            for power in range(LOG - 1, -1, -1):
                if jump[power][current] < right:
                    current = jump[power][current]
                    distance += 1 << power
            if farthest[current] >= right:
                answer.append(distance + 1)
            else:
                answer.append(-1)
        return answer