import math


class graph:

    def __init__(self):
        self.dictionary = {}            #Dictionary for edges and adjacent edges

    def addVertex(self, vertex):
        #Function to add a vertex to the graph
        if vertex not in self.dictionary:
            self.dictionary[vertex] = []
        else:
            print("Cannot have two vertices with the same label.")

    def addEdge(self,vertex1,vertex2,weight):
        #Funtion to add an edge to the graph using the two vertices as reference
        self.dictionary[vertex1].append(vertex2)        #Add edge as adjacent
        self.dictionary[vertex2].append(vertex1)        #Add edge as adjacent
        
    def printDict(self):
        #Function to print out the graph dictionary in a readable form
        print("Edges:")
        for key in self.dictionary:
            print(key, ":", self.dictionary[key])
    
    def DFS(self, vertex):
        #Function to perform a Depth First Search
        stack = []                  #Stack for unvisited vertices
        visited = []                #List of visited vertices
        stack.append(vertex)
        while stack != []:
            u = stack.pop()
            if u not in visited:
                visited.append(u)
                for e in self.dictionary[u]:
                    stack.append(e)         #Add adjacent vertices to stack
        f = open("DFS.txt", "w")
        f.write("DFS Traversal: %s " % visited)     #Write DFS path to text file
        f.close()
        return visited
    
    def BFS(self, vertex):
        #Function to perform a Breadth First Search
        queue = []                  #Queue for unvisited vertices
        visited = []                #List of visited vertices
        queue.insert(0, vertex)
        while queue != []:
            u = queue.pop()
            if u not in visited:
                visited.append(u)
                for e in self.dictionary[u]:
                    queue.insert(0, e)      #Add adjacent vertices to queue
        f = open("BFS.txt", "w")
        f.write("BFS Traversal: %s " % visited)     #Write BFS path to text file
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
