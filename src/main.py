from node import Node
from graph import Graph

def initializeGraph(filename):
    # Baca File
    f = open("test/" + filename)

    fileArr = f.read().splitlines()
    numOfNodes = int(fileArr[0])
    nodeList = fileArr[1:numOfNodes]
    fileMatrix = fileArr[numOfNodes+1:]
    adjacencyMatrix = [ [ 0 for i in range(numOfNodes) ] for j in range(numOfNodes) ]
    # Init graph
    graph = Graph(numOfNodes)

    # Tambahkan node dari file txt
    for i in range(numOfNodes-1):
        splitString = nodeList[i].split(" ", 2)
        newNode = Node(splitString[0], splitString[1], splitString[2])
        graph.addNode(newNode)
        adjacencyMatrix[i] = [int(x) for x in fileMatrix[i].split(" ")]

    graph.addAdjacency(adjacencyMatrix)
    
    return graph

# Main Program
filename = input("Masukkan filename: ")
graph = initializeGraph(filename)

graph.printGraph()
graph.printAdjacency()