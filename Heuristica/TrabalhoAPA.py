import random
from GrafosTeste import graph_dict3
from GrafosTeste import graph_dict1

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
                            
g1 = Graph(graph_dict1)
g2 = Graph(graph_dict3)

def GraphColoringBad(G):
    c = [-1]*len(G.vertices())#iniciliza o array de cores com -1, que significa sem cor

    for v in range(0, len(G.vertices())):
        c[v] = v

    return ColorsUsed(c),c

def GraphColoringGrade(G):
     c = [-1]*len(G.vertices())
     

     for v in G.verticesByGrade():
         c[v] = 0
         while(not(G.safe(v,c))):
             c[v] = c[v] + 1
                             
     return c

def ColorList(color):
    cl = [[] for _ in range(max(color) + 1)]# ou xrange
    i = 0

    while(i <= max(color)):
        for j in range(0,len(color)):
            if(color[j] == i):
                cl[i].append(j)
        i = i + 1
    return cl

def ColorsUsed(color):
    clSize = ColorList(color)

    return len(clSize)

def CheckSolution(G, color):

    for v in G.vertices():
        if(not(G.safe(v, color))):
            print("Invalido")
            return 0
        
    print("Valido")
    

def RandomGraphColoring(G, alpha):
    c = [-1]*len(G.vertices())
    v = G.verticesByGrade()

    filtro = int(len(v) - (len(v)*alpha))
    sortedList = v[0:filtro+1]
    randomList = v[filtro+1:len(v)]
    
    for i in sortedList:
        c[i] = 0
        while(not(G.safe(i,c))):
            c[i] = c[i] + 1

    while(randomList):
        j = random.choice(randomList)
        c[j] = 0
        while(not(G.safe(j,c))):
            c[j] = c[j] + 1
        randomList.remove(j)
        
    return ColorsUsed(c),c
        
def MV(G, color):
    busca = max(color)
    newColor = color
    nova = 0

    cl = ColorList(newColor)
    
    while(busca >= 1):
        for v in cl[busca]:
            while(nova <= busca):
                newColor[v] = nova
                if(G.safe(v, newColor)):
                    cl[busca].remove(v)
                    cl[nova].append(v)
                    break
                else:
                    nova = nova + 1

        if(not(cl[busca])):
            busca = max(newColor)
        else:
            busca = busca - 1
            nova = 0

    return ColorsUsed(newColor), newColor

def GRASP(G, iteracoes, alpha):
    condicaoParada = 0
    sBest, best = GraphColoringBad(G)

    while(condicaoParada <= iteracoes):
        s1, cores = RandomGraphColoring(G, alpha)
        s2, novasCores = MV(G, cores)
       
        if(s2 < sBest):
            best = novasCores
            
        condicaoParada = condicaoParada + 1

    return best


cor1 = [0,1,2,0,2,3,1,4]
cl, cor2 = MV(g,cor1)
nc, c = RandomGraphColoring(g, 1)

b = GRASP(g, 1000, 1)
CheckSolution(g, cor1)
