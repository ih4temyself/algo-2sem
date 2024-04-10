import graph
from graph_search import Graph_search


class DFS(Graph_search):
    def __init__(self, graph, source):
        super().__init__(graph, source)
        self._dbfs(source)

    @staticmethod
    def get_next(stack):
        return stack.pop()


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
    dfs = DFS(graph, source)
    for i in range(0, graph.vertex_count()):
        path = dfs.path_to(i)
        if path:
            print(path)
        else:
            print(f"{source} not connected with {i}")
