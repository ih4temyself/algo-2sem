from abc import ABC, abstractmethod


class Graph_search(ABC):
    def __init__(self, graph, source):
        self._graph = graph
        self._source = source
        self._edge_to = []
        self._marked = []
        for i in range(graph.vertex_count()):
            self._edge_to.append(None)
            self._marked.append(False)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while x != self._source:
            path.append(x)
            x = self._edge_to[x]
        path.append(self._source)
        path.reverse()
        return path

    def _dbfs(self, v):
        self._marked[v] = True
        stack = [v]
        while len(stack) > 0:
            x = self.get_next(stack)
            for w in self._graph.adj(x):
                if not self._marked[w]:
                    stack.append(w)
                    self._marked[w] = True
                    self._edge_to[w] = x

    @abstractmethod
    def get_next(stack):
        raise NotImplementedError
