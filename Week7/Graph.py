import math


class graph:

    def __init__(self):
        self.dictionary = {}
        self.weights = {}
        self.tentative = {}
        self.previous = {}

    def addVertex(self, vertex):
        if vertex not in self.dictionary:
            self.dictionary[vertex] = []
        else:
            print("Cannot have two vertices with the same label.")

    def addEdge(self,vertex1,vertex2,weight):
        self.dictionary[vertex1].append(vertex2)
        self.dictionary[vertex2].append(vertex1)
        # print(self.dictionary)
        self.weights[vertex1,vertex2] = weight

    def printDict(self):
        print("Edges:")
        for key in self.dictionary:
            print(key, ":", self.dictionary[key])
        print("")
        print("Weights:")
        for key in self.weights:
            print(key, ":", self.weights[key])
    
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
            print(u)
            if u not in visited:
                visited.append(u)
                for e in self.dictionary[u]:
                    queue.insert(0, e)
        f = open("BFS.txt", "w")
        f.write("BFS Traversal: %s " % visited)
        f.close()
        return visited

    """
    def dijkstra(self, source, dest):
        current = source
        done = False
        for node in self.dictionary:
            self.tentative[node] = float("inf")
        self.tentative[source] = 0
        visited = []
        path = [source]
        nextNode = 0
        while done == False:
            print("CURRENT:")
            print(current)
            for adjacent in self.dictionary[current]: 
                try:        # try loop for retrieving weights, key is a list so trying both combinations of lists for 2 elements
                    w = self.weights[adjacent, current]
                except KeyError:
                    w = self.weights[current, adjacent]
                print("current:" + str(current) + " adjacent:" + str(adjacent) + " weight:"+ str(w))
                if (self.tentative[current] + w) < self.tentative[adjacent]:
                    self.tentative[adjacent] = self.tentative[current] + w
                    #self.previous[adjacent] = current
                print("Current weight for node ", adjacent, ": ", self.tentative[adjacent])
            visited.append(current)
            minimum = float("inf")
            for node in self.dictionary[current]:
                print("======")
                print("Node: ", node)
                print("Current: ", current)
                print("Minimum: ", minimum)
                print("Next: ", nextNode)
                print("======")
                if node == dest and self.tentative[node] < self.tentative[current]:
                    current = node
                    path.append(node)
                    done = True
                    
                elif node not in visited and self.tentative[node] < minimum:
                    nextNode = node
                    minimum = self.tentative[node]
                    print(minimum)
                    #path.append(node)
            if nextNode == current:
                path.reverse()
                print("Removing ", current)
                path.remove(current)
                path.reverse()
                current = self.previous[current]
            else:
                self.previous[nextNode] = current
                current = nextNode
                path.append(current)
                
        print("==============")
        print("Correct output for example:")
        print("[1, 2, 5, 7, 6]")
        print("==============")
        print("Actual output")
        print("Visited: ", visited)
        print("Path: ", path)
        print(path[0:(path.index(dest)+1)])
    """

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
