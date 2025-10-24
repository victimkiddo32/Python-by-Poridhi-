class Solution:
    def graphColoring(self, v, edges, m):
        # Build adjacency list
        graph = {i: [] for i in range(v)}
        for u, w in edges:
            graph[u].append(w)
            graph[w].append(u)  # undirected

        color = [0] * v

        def isSafe(node, c):
            for neighbour in graph[node]:
                if color[neighbour] == c:
                    return False
            return True

        def backtrack(node):
            if node == v:  # all vertices colored
                return True

            for c in range(1, m + 1):  # colors 1..m
                if isSafe(node, c):
                    color[node] = c
                    if backtrack(node + 1):
                        return True
                    color[node] = 0  # backtrack

            return False

        return backtrack(0)


if __name__ == "__main__":
    v = 4
    edges = [[0,1], [1,2], [2,3], [3,0], [0,2]]
    m = 3

    sol = Solution()
    print(sol.graphColoring(v, edges, m))