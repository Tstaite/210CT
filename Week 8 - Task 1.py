from collections import defaultdict #import defaultdict function only
listofNodes=[]

class newVertex: #class to create each node
    def __init__(self, value):
        self.value = value
        listofNodes.append(value)

class Graph: #class to create a graph
    def __init__(self, Nodes):
        self.nodes = {} 
        for i in Nodes:
            self.nodes[i] = []
        
        self.edges = defaultdict(list) #initial value for default dict. is a list
        self.distance = {}

        
    def new_node(self, value): #function to add node
        self.nodes[value] = []
        

    def new_edge(self, from_node, to_node, distance): #function to add edge
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distance[(from_node, to_node)] = distance


def Dijkstra (graph, start_node, end_node):
    v = start_node
    testingList=()
    distances = {}
    for i in graph.edges[v]:
        distances[i] = float('inf')
    distances[v] = 0
    visited = []
    while v != end_node:
        for k in graph.edges[v]:
            new_distance = distances[start_node] + graph.distance [(start_node, i)]
            if new_distance < distances.get(k, float('inf')):
                distances[i] = new_distance
                testingList[k] = v

        visited.append(v)
        newmin = float('inf')
        for a in v:
            if a not in visited and distances[a] < newmin:
                v = a
                newmin = distances[a]
        



if __name__ == '__main__':
    
    
    myList = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] #nodes for the graph
    for element in myList:
        newVertex(element)

    #create graph, add nodes and add edges
    myGraph=Graph(listofNodes)
    myGraph.new_node('H')
    myGraph.new_edge('A', 'B', 13)
    myGraph.new_edge('B', 'A', 13)
    
    myGraph.new_edge('B', 'C', 22)
    myGraph.new_edge('C', 'B', 22)
    
    myGraph.new_edge('B', 'D', 34)
    myGraph.new_edge('D', 'B', 34)
    
    myGraph.new_edge('B', 'E', 10)
    myGraph.new_edge('E', 'B', 10)
    
    myGraph.new_edge('E', 'C', 2)
    myGraph.new_edge('C', 'E', 2)

    myGraph.new_edge('E', 'F', 16)
    myGraph.new_edge('F', 'E', 16)

    myGraph.new_edge('F', 'G', 44)
    myGraph.new_edge('G', 'F', 44)

    myGraph.new_edge('G', 'H', 21)
    myGraph.new_edge('H', 'G', 21)

    Dijkstra(myGraph, 'B', 'F')
  

    
