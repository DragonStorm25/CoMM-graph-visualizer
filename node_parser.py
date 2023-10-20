

if __name__ == "__main__":
    input_file_path = "nodes.txt"
    input_file = open(input_file_path, "r")
    input_file_text = input_file.read()

    edge_list = input_file_text.split("\n")
    for edge in edge_list:
        print(edge)