from math import radians, cos, sin, asin, sqrt

class Astar:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.yet_visited = []
        self.visited = []

    def haversine(self, node1, node2):
        # convert decimal degrees to radians 
        R = 6372.8 # Dalam km

        dLat = radians(node2.getLat() - node1.getLat())
        dLon = radians(node2.getLong() - node1.getLong())
        lat1 = radians(node1.getLat())
        lat2 = radians(node2.getLat())

        a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
        c = 2*asin(sqrt(a))

        return R * c

    # Tampilkan path solusi
    def get_path(self):
        return

    
