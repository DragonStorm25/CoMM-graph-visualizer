import GraphVisualizer

if __name__ == "__main__":
    # Create graph visualizer
    G = GraphVisualizer.GraphVisualizer()

    # Read and store node text
    node_file_path = "nodes.txt"
    node_file = open(node_file_path, "r")
    node_file_text = node_file.read()

    # TODO Add options for required (*), optional (?), and helpful (!) links
    # TODO Add names OR groups and assign unique color to each group

    # Parse node text and add all edges
    edge_list = node_file_text.split("\n")
    for edge in edge_list:
        edge_info_pieces = edge.strip().split(" ")
        edge_head = edge_info_pieces[-1]
        edge_tail = edge_info_pieces[-3] # Skip -2, as that's the arrow
        G.addEdge(edge_tail, edge_head)

    # Read and store tooltip text
    tooltip_file_path = "tooltip.txt"
    tooltip_file = open(tooltip_file_path, "r")
    tooltip_file_text = tooltip_file.read()

    # Parse tooltip text and add all labels
    tooltip_list = tooltip_file_text.split("\n")
    for tooltip in tooltip_list:
        node, text = tooltip.split(" = ")
        G.addLabel(node, text)

    # Visualize graph
    G.visualize()
