import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization: 
   
    def __init__(self): 
        self.visual = [] 
          
    def addEdge(self, a, b): 
        temp = [a, b] 
        self.visual.append(temp) 

    def visualize(self): 
        G = nx.DiGraph() 
        G.add_edges_from(self.visual) 
        nx.draw_kamada_kawai(G, with_labels=True) 
        plt.show() 

if __name__ == "__main__":
    input_file_path = "nodes.txt"
    input_file = open(input_file_path, "r")
    input_file_text = input_file.read()

    G = GraphVisualization()
    edge_list = input_file_text.split("\n")
    for edge in edge_list:
        edge_tail, edge_head = edge.replace(" ", "").split("->")
        print(f"tail: {edge_tail}, head: {edge_head}")
        G.addEdge(edge_tail, edge_head)
    G.visualize()
