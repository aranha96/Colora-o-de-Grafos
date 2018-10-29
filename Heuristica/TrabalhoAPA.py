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

    def safe(self, vertice, color):
        for n in self.edges(vertice):
            if color[vertice] == color[n]:
                return False
        return True

    def verticesByGrade(self):
        grade = self.grade()
        vertice = self.vertices()
        
        vg = [v for _, v in sorted(zip(grade, vertice), reverse=True)]

        return vg
    
                        
g = Graph(graph_dict1)

def GraphColoringBad(G):
    c = [-1]*len(G.vertices())#iniciliza o array de cores com -1, que significa sem cor

    for v in range(0, len(G.vertices())):
        c[v] = v

    return c

def GraphColoringGrade(G):
     c = [-1]*len(G.vertices())
     

     for v in G.verticesByGrade():
         c[v] = 0
         while(not(G.safe(v,c))):
             c[v] = c[v] + 1
                             
     return c

def ColorList(color):
    cl = [[] for _ in xrange(max(color) + 1)]
    i = 0

    while(i <= max(color)):
        for j in range(0,len(color)):
            if(color[j] == i):
                cl[i].append(j)
        i = i + 1
    return cl

def ColorsUsed(color):
    clSize = ColorList(color)

    return clSize

#def CheckSolution(oldSolution, color):
#    newSolution = max(color) + 1
#    
#    if (newSolution < oldSolution):
#        print("Solucao melhorada")
#    else:
#        print("Nao ocorreu melhora")

def RandomGraphColoring(G, alpha):
    c = [-1]*len(G.vertices())
    v = G.verticesByGrade()
# criar fator randomico em v
    for i in v:
        c[i] = 0
        while(not(G.safe(i,c))):
            c[i] = c[i] + 1
            
    return c
        
def MV(G, color):
    busca = max(color)
    os = busca + 1
    nova = 0

    cl = ColorList(color)
    
    while(busca > 1):
        for v in cl[busca]:
            while(nova <= busca):
                color[v] = nova
                if(G.safe(v, color)):
                    break
                else:
                    nova = nova + 1
        busca = busca - 1
        nova = 0
        
def GRASP(G):
    condicaoParada = 0
    best = []

    while(condicaoParada):
        sol = GraphColoringGrade(G)
        s1 = ColorsUsed
        sol = MV(G, sol)
        s2 = ColorsUsed
        if(s2 < s1):
            best.append(sol)

#cor1 = GraphColoringGrade(g)
#cor2 = GraphColoringBad(g)
#MV(g, cor2)




