from node import Node
from graph import Graph
from astar import Astar

def initializeGraph(filename):
    # Baca File
    f = open("test/" + filename)

    fileArr = f.read().splitlines()
    numOfNodes = int(fileArr[0])
    nodeList = fileArr[1:numOfNodes+1]
    fileMatrix = fileArr[numOfNodes+1:]
    adjacencyMatrix = [ [ 0 for i in range(numOfNodes) ] for j in range(numOfNodes) ]
    # Init graph
    graph = Graph(numOfNodes)

    # Tambahkan node dari file txt
    for i in range(numOfNodes):
        splitString = nodeList[i].split(" ", 2)
        newNode = Node(float(splitString[0]), float(splitString[1]), splitString[2])
        graph.addNode(newNode)
        adjacencyMatrix[i] = [int(x) for x in fileMatrix[i].split(" ")]

    graph.addNeighbours(adjacencyMatrix)
    
    return graph

# Main Program
filename = input("Masukkan filename: ")
graph = initializeGraph(filename)
graph.printGraph()

# Input Lokasi
print("Masukkan rute lokasi yang ingin dicari:")
start = None
goal = None

while start == None or goal == None:
    start_node = input("Masukkan lokasi awal: ")
    start = graph.findNode(start_node)
    goal_node = input("Masukkan lokasi tujuan: ")
    goal = graph.findNode(goal_node)
    if (start == None or start == None):
        print("Masukkan tujuan lagi! Node tidak ditemukan")
    print()

# Penghitungan path yang benar
astar = Astar(graph, start, goal)
print(astar.haversine(start, goal), "km")