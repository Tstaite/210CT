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
        
    def new_node(self, value): #function to add node
        self.nodes[value] = []
        

    def new_edge(self, from_node, to_node): #function to add edge
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        



if __name__ == '__main__':
    
    
    myList = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] #nodes for the graph
    for element in myList:
        newVertex(element)

    #create graph, add nodes and add edges
    myGraph=Graph(listofNodes)
    myGraph.new_node('H')
    myGraph.new_edge('A', 'B')
    myGraph.new_edge('B', 'C')
    myGraph.new_edge('B', 'D')
    myGraph.new_edge('B', 'E')
    myGraph.new_edge('C', 'E')
    myGraph.new_edge('E', 'F')
    myGraph.new_edge('F', 'G')
    myGraph.new_edge('G', 'H')


    print(myGraph.nodes)
