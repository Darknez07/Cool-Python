import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
G = nx.DiGraph()
color_graph = ["blue" for i in range(31)]
grph = dict()
adds = []

def draw(G, color):
    write_dot(G,'test.dot')
    plt.title('Tree Traversal')
    pos = graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=True, arrows=True,font_size=10,node_color=color)
    plt.savefig('nx_test.png')
    camera.snap()

def bfs():
    for i in range(31):
        color_graph[i] = "red"
        draw(G, color_graph)

def scan(src, dest):
    try:
        if dest == src or scan(grph[src][0], dest) or scan(grph[src][1], dest):
            adds.append(src)
            return True
    except KeyError:
        return False
    return False


for i in range(31):
    G.add_node(i)

G.add_edge(0, 1)
G.add_edge(0, 2)
grph[0] = [1,2]
G.add_edge(1, 3)
G.add_edge(1, 4)
grph[1] = [3,4]
G.add_edge(2, 5)
G.add_edge(2, 6)
grph[2] = [5, 6]
G.add_edge(3, 7)
G.add_edge(3, 8)
grph[3] = [7, 8]
G.add_edge(4, 9)
G.add_edge(4, 10)
grph[4] = [9, 10]
G.add_edge(5, 11)
G.add_edge(5, 12)
grph[5] = [11, 12]
G.add_edge(6, 13)
G.add_edge(6, 14)
grph[6] =[13, 14]
G.add_edge(7, 15)
G.add_edge(7, 16)
grph[7] =[15, 16]
G.add_edge(8, 17)
G.add_edge(8, 18)
grph[8] =[17,18]
G.add_edge(9, 19)
G.add_edge(9, 20)
grph[9] = [19, 20]
G.add_edge(10, 21)
G.add_edge(10, 22)
grph[10] = [21, 22]
G.add_edge(11, 23)
G.add_edge(11, 24)
grph[11] = [23, 24]
G.add_edge(12, 25)
G.add_edge(12, 26)
grph[12] = [25, 26]
G.add_edge(13, 27)
G.add_edge(13, 28)
grph[13] = [27, 28]
G.add_edge(14, 29)
G.add_edge(14, 30)
grph[14] = [29, 30]


scan(0, 23)
adds.reverse()
bfs()

animation = camera.animate()
plt.show()
animation.save('celluloid_minimal.gif', writer = 'imagemagick')