import GraphVisualizer

if __name__ == "__main__":
    # Read and store file text
    node_file_path = "nodes.txt"
    node_file = open(node_file_path, "r")
    node_file_text = node_file.read()

    # Create graph visualizer
    G = GraphVisualizer.GraphVisualizer()

    # Parse input text and add all edges
    edge_list = node_file_text.split("\n")
    for edge in edge_list:
        edge_tail, edge_head = edge.replace(" ", "").split("->")
        G.addEdge(edge_tail, edge_head)

    tooltip_file_path = "tooltip.txt"
    tooltip_file = open(tooltip_file_path, "r")
    tooltip_file_text = tooltip_file.read()

    G.addLabel("18.01", "Calculus 1 and 2")

    # Visualize graph
    G.visualize()
