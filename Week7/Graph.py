class graph:
    def __init__(self):
        self.dictionary = {}
    def addVertex(self, vertex):
        if vertex not in self.dictionary:
            self.dictionary[vertex] = []
        else:
            print("Fuck Off")
    def addEdge(self,vertex1,vertex2):
        self.dictionary[vertex1].append(vertex2)
        self.dictionary[vertex2].append(vertex1)
        #print(self.dictionary)

    def printDict(self):
        for key in self.dictionary:
            print(key, ':', self.dictionary[key])
    
    def DFS(self, vertex):
        stack = []
        visited = []
        stack.append(vertex)
        while stack != []:
            u = stack.pop()
            if u not in visited:
                visited.append(u)
                for e in self.dictionary[u]:
                    stack.append(e)
        return visited
    
    def BFS(self, vertex):
        queue = []
        visited = []
        queue.insert(0, vertex)
        while queue != []:
            u = queue.pop()
            print(u)
            if u not in visited:
                visited.append(u)
                for e in self.dictionary[u]:
                    queue.insert(0, e)
        return visited

    def dijkstra(self, source, dest):
        v = source


g = graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addEdge(1,2)
g.addEdge(2,5)
g.addEdge(3,4)
g.addEdge(2,6)
g.addEdge(5,6)
g.addEdge(1,3)
g.addEdge(3,7)
g.addEdge(6,7)
g.printDict()
