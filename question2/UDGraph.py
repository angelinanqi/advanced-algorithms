class UDGraph:
    def __init__(self):
        self.graph = dict()  # dictionary to hold vertices and their neighbours

    def addVertex(self, vertex):
        if vertex not in self.graph:  # add vertex if it doesn't exist
            self.graph[vertex] = []

    def addEdge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:  # both vertices must exist
            self.graph[from_vertex].append(to_vertex)  # add directed edge
        else:
            raise ValueError("One or both vertices not in graph")

    def listOutgoingAdjacentVertex(self, vertex):
        return self.graph.get(vertex, [])  # return neighbours of vertex

    def hasVertex(self, vertex):
        return vertex in self.graph  # check if vertex exists

    def hasEdge(self, from_vertex, to_vertex):
        if from_vertex in self.graph:
            return to_vertex in self.graph[from_vertex]  # check if edge exists
        return False

    def getAllVertices(self):
        return list(self.graph.keys())  # list of all vertices

    def getAllEdges(self):
        edges = []
        for from_vertex, neighbours in self.graph.items():
            for to_vertex in neighbours:
                edges.append((from_vertex, to_vertex))  # collect all edges
        return edges

    def removeEdge(self, from_vertex, to_vertex):
        if from_vertex in self.graph:
            if to_vertex in self.graph[from_vertex]:
                self.graph[from_vertex].remove(to_vertex)  # remove edge
            else:
                print(f"Edge {from_vertex}->{to_vertex} does not exist.")
        else:
            print(f"Vertex {from_vertex} does not exist.")

    def removeVertex(self, vertex):
        if vertex not in self.graph:
            print(f"Vertex {vertex} does not exist.")
            return
        for neighbours in self.graph.values():  # remove vertex from all neighbour lists
            if vertex in neighbours:
                neighbours.remove(vertex)
        del self.graph[vertex]  # delete vertex itself

    def printGraph(self):
        for vertex, neighbours in self.graph.items():  # print each vertex and its neighbours
            print(f'{vertex} -> {neighbours}')


if __name__ == "__main__":
    graph = UDGraph()

    # add vertices
    graph.addVertex('A')
    graph.addVertex('B')
    graph.addVertex('C')
    graph.addVertex('D')

    # add edges
    graph.addEdge('A', 'B')
    graph.addEdge('A', 'C')
    graph.addEdge('B', 'C')
    graph.addEdge('C', 'D')

    # print graph
    graph.printGraph()

    # check outgoing neighbours
    print("Outgoing from A:", graph.listOutgoingAdjacentVertex('A'))
    print("Outgoing from B:", graph.listOutgoingAdjacentVertex('B'))

    # check vertex and edge existence
    print("Does vertex 'A' exist?", graph.hasVertex('A'))
    print("Does edge A->C exist?", graph.hasEdge('A', 'C'))

    # remove edge and vertex
    graph.removeEdge('A', 'C')
    graph.removeVertex('D')
    print("\nGraph after removals:")
    graph.printGraph()
