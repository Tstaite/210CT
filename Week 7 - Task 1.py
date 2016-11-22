graphMappings = {} #dict to store final mappings

class Vertex(object):

    #function to create nodes
    def __init__(self, label, edges):
        self.label = label
        self.edges = edges
        graphMappings[self.label] = self.edges


class Graph(object):
    
    #function to create mappings
    def create(self,myNodes):
        for element in myNodes:
            edges = []
            quantity = int(input("How many edges for node " + str(element)+"? "))
            for b in range(quantity):
                newEdge = int(input("Enter an edge "))
                edges.append(newEdge)
            Vertex(element, edges) #call Vertex function with node no. and list of edges
        

    #function to add new node
    def newNode(self, aNode):
        Vertex(aNode, [])


    #function to add new arc
    def newArc(self,startNode,endNode):
        graphMappings[startNode].append(endNode)


myNodes = [1,2,3,4,5,6,7,8,9,10] #list of nodes that need mappings

#create object, call .create function, add new node and add new arc
newGraph = Graph()
newGraph.create(myNodes)
newGraph.newNode(11)
newGraph.newArc(11,2)
print(graphMappings)
