graph_dict1 = {}

graph_dict1[0] = [1,4]
graph_dict1[1] = [0,2,4]
graph_dict1[2] = [1]
graph_dict1[3] = [4,5,6]
graph_dict1[4] = [0,1,3]
graph_dict1[5] = [3,6]
graph_dict1[6] = [3,5,7]
graph_dict1[7] = [6]

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def vertices(self):
        return list(self.graph.keys())
    
    def edges(self, vertice):
        return self.graph[vertice]

    def grade(self):
        g = [0]*len(self.vertices())
        for v in self.vertices():
            g[v] = len(self.edges(v))
        return g
                
g = Graph(graph_dict1)


def GraphColoringBad(G):
    c = [-1]*len(G.vertices())#iniciliza o array de cores com -1, que significa sem cor

    for v in range(0, len(G.vertices())):
        c[v] = v

    return c

def GraphColoring(G):
     c = [-1]*len(G.vertices())
     

     for v in G.vertices():
         c[v] = 0
         for n in G.edges(v):
             if c[v] == c[n]:
                 c[v] = c[v] + 1
        
     return c
         
def GraphColoringGrade(G):
    c = [-1]*len(G.vertices())
    g = G.grade()
    #utilizar a function max
