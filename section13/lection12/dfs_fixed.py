import digraph


class DFS:
    def __init__(self, graph):
        self._graph = graph
        self.top_ord = []
        self._edge_to = []
        self._marked = []
        for i in range(graph.vertex_count()):
            self._edge_to.append(None)
            self._marked.append(False)

        for v in range(graph.vertex_count()):
            if not self._marked[v]:
                self._dfs(v)
        self.top_ord.reverse()

    def _dfs(self, v):
        self._marked[v] = True
        for w in self._graph.adj(v):
            if not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(w)
        self.top_ord.append(v)


if __name__ == "__main__":
    graph = digraph.DiGraph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 5)
    graph.add_edge(6, 0)
    graph.add_edge(6, 4)
    graph.add_edge(3, 4)
    graph.add_edge(3, 2)
    graph.add_edge(3, 5)
    graph.add_edge(3, 6)
    graph.add_edge(5, 2)
    graph.add_edge(1, 4)

    print(graph)
    dfs = DFS(graph)
    print(dfs.top_ord)

    print("=============")

    graph2 = digraph.DiGraph()
    graph2.add_edge(0, 2)
    graph2.add_edge(0, 6)

    graph2.add_edge(1, 0)

    graph2.add_edge(2, 3)
    graph2.add_edge(2, 4)

    graph2.add_edge(3, 2)
    graph2.add_edge(3, 4)

    graph2.add_edge(4, 5)
    graph2.add_edge(4, 6)
    graph2.add_edge(4, 11)

    graph2.add_edge(5, 0)
    graph2.add_edge(5, 3)

    graph2.add_edge(6, 8)
    graph2.add_edge(8, 6)
    graph2.add_edge(6, 7)
    graph2.add_edge(9, 6)
    graph2.add_edge(9, 7)

    graph2.add_edge(9, 12)
    graph2.add_edge(10, 9)
    graph2.add_edge(12, 10)
    graph2.add_edge(12, 11)
    graph2.add_edge(11, 9)

    print(graph2)
    dfs = DFS(graph2)
    print(dfs.top_ord)
