graph_dict = {}

graph_dict[0] = [1,4]
graph_dict[1] = [0,2,4]
graph_dict[2] = [1]
graph_dict[3] = [4,5,6]
graph_dict[4] = [0,1,3]
graph_dict[5] = [3,6]
graph_dict[6] = [3,5,7]
graph_dict[7] = [6]

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def vertices(self):
        return list(self.graph.keys())
    
    def edges(self, vertice):
        return self.graph[vertice]


g = Graph(graph_dict)

def GraphColoringBad(G):

    c = [-1]*len(G.vertices())#iniciliza o array de cores com -1, que significa sem cor

    for v in range(0, len(G.vertices())):
        c[v] = v

    return c


def GraphColoring(G):
     c = [-1]*len(G.vertices())
     

     for v in G.vertices():
         for n in G.edges(v):
             if c[v] == c[n] and c[n] != -1:
                 c[v] = 0
             else:
                 c[v] = c[n] + 1
     return c
         

saida = GraphColoring(g)
print(saida)
