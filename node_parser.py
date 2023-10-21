import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    input_file_path = "nodes.txt"
    input_file = open(input_file_path, "r")
    input_file_text = input_file.read()

    G = nx.DiGraph()
    edge_list = input_file_text.split("\n")
    for edge in edge_list:
        edge_tail, edge_head = edge.replace(" ", "").split("->")
        print(f"tail: {edge_tail}, head: {edge_head}")
        G.add_edge(edge_tail, edge_head)
    nx.draw(G)
