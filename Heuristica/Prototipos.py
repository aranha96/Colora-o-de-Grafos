import random

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

def CheckSolution(oldSolution, color):
    newSolution = max(color) + 1
    
    if (newSolution < oldSolution):
        print("Solucao melhorada")
    else:
        print("Nao ocorreu melhora")

#Treino com lista de listas
    
lista1 = [1,2,3,5,6,8,7,9]
lista2 = [2,5,8,3,6,9]

listalista = []

listalista.append(lista1)
listalista.append(lista2)

#Treino com numeros aleatorios

while(lista1):
    
    v = random.choice(lista1)
    lista1.remove(v)

#Treino para o filtro

filtro = int(len(lista2) - (len(lista2)*0.5))
seg1 = lista2[0:filtro]
seg2 = lista2[filtro:len(lista2)]

