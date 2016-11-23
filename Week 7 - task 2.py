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

    #Perform Breadth-First-Search
    def BFS(self,graph,startNode, finalPath=[]):
        myQueue=[startNode] #myQueue starts with first item
        while len(myQueue) > 0: #while myQueue is not empty
            value=myQueue.pop(0) #pop item
            if value not in finalPath: #if popped item is not in final path
                finalPath=finalPath+[value] 
                myQueue=myQueue+graph[value] #myQueue is set to myQueue + nodes connected to 'value'
        print (finalPath)
            

    #Perform Depth-First-Search
    def DFS(self,graph,startNode, finalPath=[]):
        myQueue = [startNode] #myQueue starts with first item
        while len(myQueue) > 0: #while myQueue is not empty
            value=myQueue.pop(0) #pop item
            if value not in finalPath: #if popped item is not in final path
                finalPath = finalPath+[value]
                myQueue=graph[value]+myQueue #myQueue is set to nodes connected to value + myQueue
        print(finalPath)
            


myNodes = [1,2,3,4,5,6,7,8,9,10] #list of nodes that need mappings

#create object, call .create function, add new node and add new arc
newGraph = Graph()
newGraph.create(myNodes)
newGraph.DFS(graphMappings,1)


