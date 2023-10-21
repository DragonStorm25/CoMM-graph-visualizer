import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer: 
   
    def __init__(self): 
        self.visual = [] 
        self.labels = {}
        self.highlighted_nodes = set()
        self.selected = None
          
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
            # Clear axis and grab new axis
            old_view_lim = plt.gca().viewLim
            old_view_lim_x = [old_view_lim.x0, old_view_lim.x1]
            old_view_lim_y = [old_view_lim.y0, old_view_lim.y1]
            plt.cla()
            ax = plt.gca()
            ax.set_xlim(old_view_lim_x)
            ax.set_ylim(old_view_lim_y)
            # Set colors of nodes depending on highlight state
            colors = ['#cc6666' if node_name in self.highlighted_nodes else '#6666cc99' for node_name in list(G.nodes)]
            # Draw graph
            nx.draw(G, pos, node_color=colors, with_labels=True, node_size=[len(v) ** 2 * 60 for v in G.nodes()], ax=ax, edgecolors="#000000")
            plt.draw()

        # Create graph and add all edges
        G = nx.DiGraph() 
        G.add_edges_from(self.visual) 
        # Start with circle layout for consistent generation, then use circle layout to make readable layout
        circle_pos = nx.planar_layout(G)
        pos = nx.arf_layout(G, pos=circle_pos, a=5)
        fig,ax = plt.subplots() 
        nodes = nx.draw_networkx_nodes(G, pos=pos, node_size=[len(v) ** 2 * 60 for v in G.nodes()], ax=ax)
        # Draw graph
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
                if cont: # If mouse is over a node, draw highlights and tooltip
                    node_name = list(G.nodes())[ind["ind"][0]]
                    connected_nodes = set(nx.generators.ego_graph(G, node_name, radius=1).nodes()) 
                    if self.selected is not None:
                       connected_nodes |= set(nx.generators.ego_graph(G, self.selected, radius=1).nodes())
                    if self.highlighted_nodes != connected_nodes:
                        self.highlighted_nodes = connected_nodes
                        redraw()

                    update_annot(ind)
                    annot.set_visible(True)
                        
                else: # Otherwise, don't draw anything special
                    if vis:
                        connected_nodes = set() 
                        if self.selected is not None:
                            connected_nodes |= set(nx.generators.ego_graph(G, self.selected, radius=1).nodes())
                        if self.highlighted_nodes != connected_nodes:
                            self.highlighted_nodes = connected_nodes
                            redraw()
                        annot.set_visible(False)

        def click(event):
            if event.inaxes == ax:
                cont, ind = nodes.contains(event)
                if cont: # If mouse is over a node, 
                    node_name = list(G.nodes())[ind["ind"][0]]
                    self.selected = node_name
                else: # Otherwise, 
                    self.selected = None

        # Add hover event to canvas
        fig.canvas.mpl_connect("motion_notify_event", hover)
        fig.canvas.mpl_connect("button_press_event", click)
        plt.show()