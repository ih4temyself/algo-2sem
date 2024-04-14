from graph_utils.dbfs import DFS, BFS
from graph_utils.graph import Graph
import random, math


def generate_maze(num_vertices, local_probability=0.6, distant_probability=0.02):
    maze = Graph()
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            distance = abs(j - i)
            probability = (
                local_probability * math.exp(-distance / 5) + distant_probability
            )
            if random.random() < probability:
                maze.add_edge(i, j)
    return maze


def place_lamp(maze):
    possible = [i for i in range(maze.vertex_count()) if maze.degree(i) > 0]
    lamp_position = random.choice(possible)
    return lamp_position


if __name__ == "__main__":
    num_vertices = 10
    graph = generate_maze(num_vertices)
    lamp_position = place_lamp(graph)
    print(f"lamp on vertex{lamp_position}")
    print(graph)

    source = 0

    dfs = DFS(graph, source)
    bfs = BFS(graph, source)

    print("dfs path to lamp", dfs.path_to(lamp_position))
    print("bfs path to lamp:", bfs.path_to(lamp_position))
