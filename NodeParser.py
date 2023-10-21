import GraphVisualizer

if __name__ == "__main__":
    input_file_path = "nodes.txt"
    input_file = open(input_file_path, "r")
    input_file_text = input_file.read()

    G = GraphVisualizer.GraphVisualizer()
    edge_list = input_file_text.split("\n")
    for edge in edge_list:
        edge_tail, edge_head = edge.replace(" ", "").split("->")
        G.addEdge(edge_tail, edge_head)
    G.addLabel("18.01", "Calculus 1 and 2")
    G.visualize()
