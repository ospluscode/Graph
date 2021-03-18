# Graph Data structure is created with Vertices and Edges
# Its used to represent networks: social media, maps ...
# Graphs can be represented by Adjacency Matrix - 2D Arrays or Adjacency List - Linked List(Dict in Py) 
# Traversal of Graph is done with Breadth First Search and Depth First Search
# BFS uses Queue and DFS uses Stack

class Graph:
    # Graph represented by Dictionary in Py (a.k.a Linked List - Adjacency List)
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    # Visit all neighbours first - horizontal search
    def BFS(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            de_vertex = queue.pop(0)
            print(de_vertex)
            for adjacent_vertex in self.graph_dict[de_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)
    

    # Visit until the end - vertical search
    def DFS(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adjacent_vertex in self.graph_dict[pop_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)