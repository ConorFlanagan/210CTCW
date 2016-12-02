import math


class graph:

    def __init__(self):
        self.dictionary = {}            #Dictionary for edges and adjacent edges

    def addVertex(self, vertex):
        if vertex not in self.dictionary:
            self.dictionary[vertex] = []
        else:
            print("Cannot have two vertices with the same label.")

    def addEdge(self,vertex1,vertex2,weight):
        self.dictionary[vertex1].append(vertex2)        #Add edge as adjacent
        self.dictionary[vertex2].append(vertex1)        #Add edge as adjacent
        
    def printDict(self):
        print("Edges:")
        for key in self.dictionary:
            print(key, ":", self.dictionary[key])
    
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
        f = open("DFS.txt", "w")
        f.write("DFS Traversal: %s " % visited)
        f.close()
        return visited
    
    def BFS(self, vertex):
        queue = []
        visited = []
        queue.insert(0, vertex)
        while queue != []:
            u = queue.pop()
            if u not in visited:
                visited.append(u)
                for e in self.dictionary[u]:
                    queue.insert(0, e)
        f = open("BFS.txt", "w")
        f.write("BFS Traversal: %s " % visited)
        f.close()
        return visited

g = graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addEdge(1,2,3)
g.addEdge(1,3,7)
g.addEdge(2,5,4)
g.addEdge(2,8,6)
g.addEdge(3,4,2)
g.addEdge(3,5,5)
g.addEdge(3,6,15)
g.addEdge(4,6,8)
g.addEdge(5,7,3)
g.addEdge(6,7,6)
g.addEdge(7,8,2)
g.printDict()
