import graph
from graph_search import Graph_search


class BFS(Graph_search):
    def __init__(self, graph, source):
        super().__init__(graph, source)
        self._dbfs(source)

    @staticmethod
    def get_next(queue):
        return queue.pop(0)


if __name__ == "__main__":
    graph = graph.Graph()
    graph.add_edge(0, 5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 6)
    graph.add_edge(6, 4)
    graph.add_edge(4, 3)
    graph.add_edge(4, 5)
    graph.add_edge(5, 3)

    print(graph)

    source = 0
    bfs = BFS(graph, source)
    for i in range(0, graph.vertex_count()):
        if bfs.has_path_to(i):
            print(bfs.path_to(i))
        else:
            print(f"{source} not connected with {i}")
