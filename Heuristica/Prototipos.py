def MVI(G, color):
    busca = max(color)
    nova = 0
    
    while(busca > 1):
        for v in G.vertices():
            if (color[v] == busca):
                while(nova <= busca):
                    color[v] = nova
                    if (G.safe(v, color)):
                        nova = busca + 1
                    else:
                        nova = nova + 1
        busca = busca - 1
        nova = 0

def GraphColoring(G):
     c = [-1]*len(G.vertices())
     

     for v in G.vertices():
         c[v] = 0
         for n in G.edges(v):
             if c[v] == c[n]:
                 c[v] = c[v] + 1
        
     return c

lista1 = [1,2,3,5,6,8,7,9]
lista2 = [2,5,8,3,6,9]

listalista = []

listalista.append(lista1)
listalista.append(lista2)

print(listalista)
