from math import radians, cos, sin, asin, sqrt
from prioqueue import PriorityQueue

def haversine(node1, node2):
    # convert decimal degrees to radians 
    R = 6372.8 # Dalam km

    dLat = radians(node2.latitude - node1.latitude)
    dLon = radians(node2.longitude - node1.longitude)
    lat1 = radians(node1.latitude)
    lat2 = radians(node2.latitude)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c
class Astar:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.frontier = PriorityQueue()
        self.came_from = {self.start: None}
        self.total_cost = {self.start: 0}

    def solve(self):
        self.start.f = 0 + haversine(self.start, self.goal)
        self.frontier.insert(self.start)
        while not self.frontier.empty():
            current = self.frontier.pop()
            if current == self.goal:
                break
        
            for neighbour in current.neighbour:
                new_cost = self.total_cost[current] + haversine(current, neighbour)
                if neighbour not in self.total_cost or new_cost < self.total_cost[neighbour]:
                    self.total_cost[neighbour] = new_cost
                    neighbour.f = new_cost + haversine(neighbour, self.goal)
                    self.frontier.insert(neighbour)
                    self.came_from[neighbour] = current

        if (self.goal not in self.came_from):
            self.came_from = {}

        return self.came_from, self.total_cost
    
    def get_path(self):
        current = self.goal
        path = [current]
        while current != self.start:
            current = self.came_from[current]
            path.append(current)

        path.reverse()
        return path
