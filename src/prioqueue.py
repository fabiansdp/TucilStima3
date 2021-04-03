class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def insert(self, item):
        self.elements.append(item)

    def pop(self):
        min = 0
        for i in range(len(self.elements)):
            if self.elements[i].f < self.elements[min].f:
                min = i
        item = self.elements[min]
        del self.elements[min]
        return item

    