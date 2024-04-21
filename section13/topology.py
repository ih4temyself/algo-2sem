from lection12.digraph import DiGraph
from lection12.dfs import DFS

class Topology():
    def __init__(self, graph):
        self.graph = graph
        self.start_point = 0
        self.stack = []