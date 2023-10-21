import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer: 
   
    def __init__(self): 
        self.visual = [] 
        self.labels = {}
        self.highlighted_nodes = set()
          
    def addEdge(self, a, b): 
        """
        Add an edge from a to b
        """
        temp = [a, b] 
        self.visual.append(temp) 

    def addLabel(self, a, label_text):
        """
        Add a label to node a, this text will be displayed when a is hovered over
        """
        self.labels[a] = label_text

    def visualize(self): 
        """
        Create the entire visual representation of the graph, with highlighting and tooltips
        """
        def redraw():
            """
            Redraw the graph. Also updates the axis variable
            """
            plt.cla()
            ax = plt.gca()
            colors = ['#cc6666' if node_name in self.highlighted_nodes else '#6666cc' for node_name in list(G.nodes)]
            nx.draw(G, pos, node_color=colors, with_labels=True, node_size=[len(v) ** 2 * 60 for v in G.nodes()], ax=ax, edgecolors="#000000")
            plt.draw()

        G = nx.DiGraph() 
        G.add_edges_from(self.visual) 
        circle_pos = nx.circular_layout(G)
        pos = nx.arf_layout(G, pos=circle_pos, a=5)
        fig,ax = plt.subplots() 
        nodes = nx.draw_networkx_nodes(G, pos=pos, node_size=[len(v) ** 2 * 60 for v in G.nodes()], ax=ax)
        redraw()
        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
        
        def update_annot(ind):
            annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
            node = ind["ind"][0]
            node_name = list(G.nodes())[node]
            xy = pos[node_name]
            annot.xy = xy
            if node_name in self.labels:
                text = self.labels[node_name]
            else:
                text = "No info"
            annot.set_text(text)

        def hover(event):
            vis = annot.get_visible()
            if event.inaxes == ax:
                cont, ind = nodes.contains(event)
                if cont:
                    node_name = list(G.nodes())[ind["ind"][0]]
                    connected_nodes = nx.generators.ego_graph(G, node_name, radius=1).nodes()
                    if self.highlighted_nodes != set(connected_nodes):
                        self.highlighted_nodes = set(connected_nodes)
                        redraw()

                    update_annot(ind)
                    annot.set_visible(True)
                        
                else:
                    if vis:
                        if self.highlighted_nodes != set():
                            self.highlighted_nodes = set()
                            redraw()
                        annot.set_visible(False)

        fig.canvas.mpl_connect("motion_notify_event", hover)
        plt.show()