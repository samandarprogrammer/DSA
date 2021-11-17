# DFS:- Depth First Search:-


class Graph:
    def __init__(self, nVertices) -> None:
        self.Nvertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def containEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def removeEdge(self, v1, v2):
        if self.containEdge is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __str__(self) -> str:
        return str(self.adjMatrix)

    def __dfsHelper(self, sv, visited):
        print(sv)
        visited[sv] = True
        for i in range(self.Nvertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.Nvertices)]
        self.__dfsHelper(0, visited)

    def __str__(self) -> str:
        return str(self.adjMatrix)


g = Graph(6)
# g.addEdge(0, 1)
# g.addEdge(1, 5)
# g.addEdge(2, 5)
# g.addEdge(2, 3)
# g.addEdge(2, 4)
# g.addEdge(0, 2)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)


print(g.adjMatrix)
g.dfs()
