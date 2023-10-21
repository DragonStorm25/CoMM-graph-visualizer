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
        circle_pos = nx.circular_layout(G)
        pos = nx.arf_layout(G, pos=circle_pos, a=5)
        fig,ax = plt.subplots() 
        nodes = nx.draw_networkx_nodes(G, pos, node_size=[len(v) ** 2 * 60 for v in G.nodes()], ax=ax)
        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
        def update_annot(ind):
            node = ind["ind"][0]
            xy = pos[list(G.nodes())[node]]
            annot.xy = xy
            node_attr = {'node': node}
            node_attr.update({node: list(G.nodes())[node]})
            text = '\n'.join(f'{k}: {v}' for k, v in node_attr.items())
            annot.set_text(text)

        def hover(event):
            vis = annot.get_visible()
            if event.inaxes == ax:
                cont, ind = nodes.contains(event)
                if cont:
                    update_annot(ind)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        fig.canvas.draw_idle()
        fig.canvas.mpl_connect("motion_notify_event", hover)
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
