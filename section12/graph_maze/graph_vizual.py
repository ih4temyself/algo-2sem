import networkx as nx
from pyvis.network import Network
from maze_lampa import generate_maze, place_lamp
from graph_utils.dbfs import DFS, BFS
import os

def visualize_path(graph, path, filename, lamp_position):
    if path is None:
        print("No path found.")
        return
    print("Visualizing path:", path)
    maze = nx.Graph()
    for i in range(graph.vertex_count()):
        maze.add_node(i, label=str(i), color="pink")
    for i in range(graph.vertex_count()):
        for j in graph.adj(i):
            if j > i:
                maze.add_edge(i, j, color="pink")

    nt = Network(
        "1000px", "1400px", notebook=True, bgcolor="#222222", font_color="white"
    )
    # nt.barnes_hut()
    nt.force_atlas_2based()
    nt.show_buttons(filter_=["physics"])
    nt.from_nx(maze)
    for n in nt.nodes:
        if n["id"] == lamp_position:
            n["shape"] = "image"
            n["image"] = "graph_maze/lamp.png"
            n["size"] = 25
    for e in nt.edges:
        if e["from"] in path and e["to"] in path:
            e["width"] = 8
            e["color"] = "green"

    nt.show(f"{filename}.html")


if __name__ == "__main__":
    num_vertices = 24
    graph = generate_maze(num_vertices)
    lamp_position = place_lamp(graph)
    print(f"lamp on vertex {lamp_position}")
    print(graph)

    source = 0
    dfs = DFS(graph, source)
    bfs = BFS(graph, source)
    dfs_path = dfs.path_to(lamp_position)
    bfs_path = bfs.path_to(lamp_position)

    visualize_path(graph, dfs_path, "dfs_path", lamp_position)
    visualize_path(graph, bfs_path, "bfs_path", lamp_position)
