import sys

#Grafos de teste

graph_dict1 = {}

graph_dict1[0] = [1,4]
graph_dict1[1] = [0,2,4]
graph_dict1[2] = [1]
graph_dict1[3] = [4,5,6]
graph_dict1[4] = [0,1,3]
graph_dict1[5] = [3,6]
graph_dict1[6] = [3,5,7]
graph_dict1[7] = [6]


graph_dict2 = {}

graph_dict2[0] = [1,2]
graph_dict2[1] = [0,2]
graph_dict2[2] = [0,1]


graph_dict3 = {}

graph_dict3[0] = [1]
graph_dict3[1] = [0,2,3]
graph_dict3[2] = [1,10]
graph_dict3[3] = [1,4]
graph_dict3[4] = [3,5]
graph_dict3[5] = [4,6]
graph_dict3[6] = [5,7,8,16]
graph_dict3[7] = [6,10]
graph_dict3[8] = [6,9,15]
graph_dict3[9] = [8,10]
graph_dict3[10] = [2,7,9,11,12,13]
graph_dict3[11] = [10]
graph_dict3[12] = [10,13]
graph_dict3[13] = [10,12,14]
graph_dict3[14] = [13,15]
graph_dict3[15] = [8,14]
graph_dict3[16] = [6,17]
graph_dict3[17] = [16,18,19]
graph_dict3[18] = [17,19]
graph_dict3[19] = [17,18]

graph_dict4 = {}

graph_dict4[0] = [1]
graph_dict4[1] = [0,5]
graph_dict4[2] = [5]
graph_dict4[3] = [5]
graph_dict4[4] = [5]
graph_dict4[5] = [1,2,3,4]

europa = {}

europa[0] = [1] #portugal
europa[1] = [0,2,3] #espanha
europa[2] = [1,3] #andorra
europa[3] = [1,2,4,5,6,7,8,10] #franca
europa[4] = [3,5,6,9] #belgica
europa[5] = [2,4,6] #luxemburgo
europa[6] = [3,4,5,7,9,11,12,13,14]#alemanha
europa[7] = [2,6,8,13,45] #suica
europa[8] = [3,7,13,15,16,17] #italia
europa[9] = [4,6] #holanda
europa[10] = [3] #monaco
europa[11] = [6,12,18,19,20,21,22] #polonia
europa[12] = [6,13,18,11] #tcheca
europa[13] = [6,7,8,12,15,18,25,45] #austria
europa[14] = [6] #dinamarca
europa[15] = [8,13,25,26] #eslovenia
europa[16] = [8] #vaticano
europa[17] = [8] #san mariono
europa[18] = [11,12,13,19,25] #eslovaquia
europa[19] = [11,18,20,21,25,27,28] #ucrania
europa[20] = [11,19,21,22,23]#belarus
europa[21] = [11,19,20,22,23,24,36,38,39,40] #russia
europa[22] = [11,20,21,23] #lituania
europa[23] = [20,21,22,24] #letonia
europa[24] = [21,23] #estonia
europa[25] = [13,15,18,19,26,27,29] #hungria
europa[26] = [15,25,29,30] #croacia
europa[27] = [19,25,28,29,31] #romenia
europa[28] = [19,27] #moldova
europa[29] = [25,26,27,30,31,32,33,34] #servia
europa[30] = [26,29,34] #bosnia
europa[31] = [27,29,32,35] #bulgaria
europa[32] = [29,31,33,35] #macedonia
europa[33] = [29,32,34,35] #albania
europa[34] = [29,30,33] #montenegro
europa[35] = [31,32,33] #grecia
europa[36] = [21,37,38] #finlandia
europa[37] = [36,38] #noruega
europa[38] = [21,36,37] #suecia
europa[39] = [21,40,41] #georgia
europa[40] = [21,39,41] #azerbaijao
europa[41] = [39,40] #armenia
europa[42] = [43] #reino unido
europa[43] = [42] #irlanda
europa[44] = [] #islandia
europa[45] = [7,13] #lichtenstein 

def CreateAdjDict():
    out = {}
    arq = open("DSJC250.9.col.txt","r")
    
    for j in arq:
        if(j[0] == 'e'):
            aux = map(int,j.split()[1:])
            for i in range(0,2): #para analizarmos nos dois sentidos da lista [1,2] e [2,1]
                if(aux[i] in out): #se existir no dicionario
                    out[aux[i]].append(aux[int(not i)]) #adicione o novo valor
                else:
                    out[aux[i]] = [aux[int(not i)]] #crie o novo elemento
    arq.close()
    return out 

graph = CreateAdjDict()
print(graph)
