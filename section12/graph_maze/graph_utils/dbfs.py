from abc import ABC, abstractmethod


class Graph_search(ABC):
    def __init__(self, graph, source):
        self._graph = graph
        self._source = source
        self._edge_to = [None] * graph.vertex_count()
        self._marked = [False] * graph.vertex_count()
        self._init_search(source)

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

    def _init_search(self, v):
        # This method should be implemented in subclasses
        raise NotImplementedError("Must be implemented by subclass")


class BFS(Graph_search):
    def _init_search(self, source):
        queue = [source]
        self._marked[source] = True
        while queue:
            v = queue.pop(0)
            for w in self._graph.adj(v):
                if not self._marked[w]:
                    queue.append(w)
                    self._marked[w] = True
                    self._edge_to[w] = v


class DFS(Graph_search):
    def _init_search(self, source):
        stack = [source]
        self._marked[source] = True
        while stack:
            v = stack.pop()
            for w in self._graph.adj(v):
                if not self._marked[w]:
                    stack.append(w)
                    self._marked[w] = True
                    self._edge_to[w] = v
