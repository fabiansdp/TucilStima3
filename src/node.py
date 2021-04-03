class Node(object):
    def __init__(self, latitude, longitude, name):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.neighbour = []
        self.f = 0

    def getLat(self):
        return self.latitude

    def getLong(self):
        return self.longitude

    def print(self):
        print("Name:", self.name)
        print("Latitude:", self.latitude)
        print("Longitude:", self.longitude)
        print("Neighbours: ", end="")
        for i in range(len(self.neighbour)):
            if i == len(self.neighbour) - 1:
                print(self.neighbour[i].name)
            else:
                print(self.neighbour[i].name, end=", ")

    def addNeighbour(self, node):
        self.neighbour.append(node)