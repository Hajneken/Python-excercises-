
class Vertex:           #reprezentuje vrchol v grafu
    def __init__(self, id, name):
        self.id = id        #numerickĂ˝ identifikĂˇtor vrcholu (int)
        self.name = name    #jmĂ©no vrcholu (String)
        self.minDistance = float('inf') #deafaultne infinity
        self.previousVertex = None
 
        self.edges = []
 
 
 
class Edge:             #reprezenetuje hranu v grafu
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
 
class Dijkstra:
    def __init__(self):
        self.vertexes = [] # this is an object
 
    def sortArray (self, stackv):
        sorted = False  # We haven't started sorting yet
        while not sorted:
            sorted = True  # Assume the list is now sorted
            for element in range(0, len(stackv)):
                try:
                    if stackv[element].minDistance > stackv[element + 1].minDistance:
                        sorted = False  # We found two elements in the wrong order
                        hold = stackv[element + 1]
                        stackv[element + 1] = stackv[element]
                        stackv[element] = hold
                except IndexError:
                    break
 
 
    def computePath(self, sourceId):
        stackv = []
        done = []
 
        for each in self.vertexes:
            if each.id == sourceId:
                each.minDistance = 0
                stackv.append(each)
            else:
                stackv.append(each)
 
        self.sortArray(stackv)
 
        while len(stackv) != 0:
            rootVertex = stackv.pop(0)
            for e in rootVertex.edges:
                target = self.getVId(e.target)
                distance = rootVertex.minDistance + e.weight
                if target.minDistance > distance:
                    target.minDistance = distance
                    target.previousVertex = rootVertex
                    done.append(target)
 
            self.sortArray(stackv)
 
        for each in self.vertexes:
            print("MinDistance to " + each.name + " is " + str(each.minDistance))
 
    def getVId(self, vertexId):
        for rootVertex in self.vertexes:
            if (rootVertex.id == vertexId):
                return rootVertex
 
    def getShortestPathTo(self, targetId):
        shortestPath = []
        return shortestPath #vrati nejkratsi cestu
 
    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = vertexes
        for e in edgesToVertexes: # e stands for edge
            for each in self.vertexes:
                if each.id == e.source:
                    each.edges.append(e)
 
    def resetDijkstra(self):
        for v in self.vertexes:
            v.minDistance = float('inf')
            v.previousVertex = None
 
    def getVertexes(self):
        return self.vertexes
 
dijkstra = Dijkstra()
list_of_vertexes = [Vertex(0, "Redville"), Vertex(1, "Blueville"), Vertex(2, "Greenville"), Vertex(3, "Orangeville"), Vertex(4, "Purpleville")]
list_of_edges = [Edge(0, 1, 9), Edge(0, 2, 1), Edge(0, 3, 4), Edge(1, 0, 5), Edge(1, 2, 3), Edge(1, 4, 3), Edge(2, 0, 3), Edge(2, 1, 3), Edge(3, 0, 7), Edge(3, 4, 1), Edge(4, 1, 8), Edge(4, 3, 8)]
dijkstra.createGraph(list_of_vertexes, list_of_edges)
dijkstra.computePath(1)
dijkstra.resetDijkstra()