class Graph(object):
    def __init__(self, numOfNodes):
        self.numOfNodes = numOfNodes
        self.nodes = []
        self.adjacency = [ [ 0 for i in range(numOfNodes) ] for j in range(numOfNodes) ]

    def addNode(self, node):
        self.nodes.append(node)

    def addAdjacency(self, matrix):
        self.adjacency = matrix

    def printGraph(self):
        for node in self.nodes:
            node.print()
            print()
    
    def printAdjacency(self):
        print(self.adjacency)