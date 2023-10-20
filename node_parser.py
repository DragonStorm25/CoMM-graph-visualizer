

if __name__ == "__main__":
    input_file_path = "nodes.txt"
    input_file = open(input_file_path, "r")
    input_file_text = input_file.read()

    edge_list = input_file_text.split("\n")
    for edge in edge_list:
        edge_tail, edge_head = edge.strip().split("->")
        print(edge_tail)
        print(edge_head)