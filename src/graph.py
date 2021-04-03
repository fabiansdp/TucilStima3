class Graph(object):
    def __init__(self, numOfNodes):
        self.numOfNodes = numOfNodes
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def printGraph(self):
        print("Daftar Node: ")
        for node in self.nodes:
            node.print()
            print()

    def addNeighbours(self, matrix):
        for i in range(self.numOfNodes):
            for j in range(self.numOfNodes):
                if matrix[i][j] != 0 :
                    self.nodes[i].addNeighbour(self.nodes[j])

    def findNode(self, name):
        for node in self.nodes:
            if (node.getName() == name):
                return node
        
            