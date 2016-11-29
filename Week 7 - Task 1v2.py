graphMappings = {} #dict to store final mappings

class Vertex(object):

    #function to create nodes
    def __init__(self, label, edges):
        self.label = label
        self.edges = edges
        graphMappings[self.label] = self.edges


class Graph(object):
    
    #function to create mappings
    def create(self,myNodes, edges):
        i = 0
        for element in myNodes:
            Vertex(element, edges[i]) #call Vertex function with node no. and list of edges
            i = i+1

    #function to add new node
    def newNode(self, aNode):
        Vertex(aNode, [])


    #function to add new arc
    def newArc(self,startNode,endNode):
        graphMappings[startNode].append(endNode)


myNodes = [1,2,3,4,5,6,7,8,9,10] #list of nodes that need mappings
edges = [[2,4],[],[1],[5,6],[],[8],[9,4],[],[2,1],[3]] #list of edges for each node


#create object, call .create function, add new node and add new arc
newGraph = Graph()
newGraph.create(myNodes, edges)
newGraph.newNode(11)
newGraph.newArc(11,2)
print(graphMappings)
