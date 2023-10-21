class GraphVisualizer: 
   
    def __init__(self): 
        self.visual = [] 
        self.labels = {}
          
    def addEdge(self, a, b): 
        temp = [a, b] 
        self.visual.append(temp) 

    def addLabel(self, a, label_text):
        self.labels[a] = label_text

    def visualize(self): 
        G = nx.DiGraph() 
        G.add_edges_from(self.visual) 
        circle_pos = nx.circular_layout(G)
        pos = nx.arf_layout(G, pos=circle_pos, a=5)
        fig,ax = plt.subplots() 
        nodes = nx.draw_networkx_nodes(G, pos=pos, node_size=[len(v) ** 2 * 60 for v in G.nodes()], ax=ax)
        nx.draw(G, pos, with_labels=True, node_size=[len(v) ** 2 * 60 for v in G.nodes()], ax=ax, edgecolors="#000000")
        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
        
        def update_annot(ind):
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
                    update_annot(ind)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        fig.canvas.draw_idle()
        fig.canvas.mpl_connect("motion_notify_event", hover)
        plt.show()