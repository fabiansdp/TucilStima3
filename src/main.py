from flask.json import jsonify
from node import Node
from graph import Graph
from astar import Astar
from flask import Flask, render_template
import json
app = Flask(__name__)

def initializeGraph(f):
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

def main(graph):
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
    came_from, total_cost = astar.solve()

    if (len(came_from) == 0):
        path = []
        distance = 0
    else:
        path = astar.get_path()
        distance = total_cost[goal]

    return start, goal, path, distance 

def processPath(path):
    name = []
    latitude = []
    longitude = []
    for i in range(len(path)):
        name.append(path[i].name)
        latitude.append(path[i].latitude)
        longitude.append(path[i].longitude)

    dictname = dict(enumerate(name))
    dicts = []
    dicts.append(dictname)

    dictlat = dict(enumerate(latitude))
    latss = []
    latss.append(dictlat)

    dictlong = dict(enumerate(longitude))
    longss = []
    longss.append(dictlong)

    return dicts, latss, longss

def processGraph(graph):
    latitude = []
    longitude = []
    for i in range(len(graph.nodes)):
        latitude.append(graph.nodes[i].latitude)
        longitude.append(graph.nodes[i].longitude)

    return latitude, longitude

def processNeighbour(graph):
    listOfDict = []
    nodes = graph.nodes
    for i in range(len(nodes)):
        listOfDict.append({
            'lat': nodes[i].latitude,
            'lng': nodes[i].longitude,
            'neighbour': []
        })
        for j in range(len(nodes[i].neighbour)):
            listOfDict[i]['neighbour'].append({
                'lat': nodes[i].neighbour[j].latitude,
                'lng': nodes[i].neighbour[j].longitude
            })
    return listOfDict

# Main program
while True:
    filename = input("Masukkan filename: ")
    # Baca File
    try:
        f = open("test/" + filename)
    except FileNotFoundError:
        print("File not found")
    else:
        break
# Inisialiasi Graph
graph = initializeGraph(f)
graph.printGraph()

# Flask
@app.route("/get-data")
def getData():
    listOfDict = processNeighbour(graph)
    return jsonify(listOfDict = listOfDict)

@app.route("/")
def init():
    # Solve Astar
    start, goal, path, distance = main(graph)
    dicts, latss, longss = processPath(path)
    marklat, marklong = processGraph(graph)
    solutionpath = json.dumps(dicts)
    arrayLat = json.dumps(latss)
    arrayLong = json.dumps(longss)
    startlat = start.latitude
    startlong = start.longitude
    destlat = goal.latitude
    destlong = goal.longitude
    sspath = path

    return render_template('map.html',  
        slat=startlat, 
        slong=startlong, 
        dlat=destlat, 
        dlong=destlong, 
        spath=solutionpath, 
        latss=arrayLat, 
        longss=arrayLong,
        sspath=sspath,
        dist = distance,
        marklat = marklat,
        marklong = marklong)
