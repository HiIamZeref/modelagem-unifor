from ortools.linear_solver import pywraplp
from reader import Reader
from pprint import pprint

# All Colors Shorterst Path

dados = Reader("grafo.txt")

solver = pywraplp.Solver.CreateSolver('SCIP')

# Criando origem e destino ficticios
origem = 0
destino = dados.qntVertices + 1

# Duplicando as arestas entre os vértices
arcos = dados.arcos + [[arco[1], arco[0], arco[2]] for arco in dados.arcos]

# Tratando os arcos
for i in range(1, dados.qntVertices + 1):
    arcos.append([origem, i, 0])
    arcos.append([i, destino, 0])



# Criando variáveis de caminho sem origem e destino ficticios
x = [[]]
for i in range(1, dados.qntVertices + 1):
    x.append([])
    for j in range(1, dados.qntVertices + 1):
            if i != j:
                x[i].append(solver.BoolVar('x[%i][%i]' % (i, j)))
            else:
                x[i].append(0)

            


# Adicionando origem e destino ficticios
for i in range(1, dados.qntVertices + 1):
    x[i].append(solver.BoolVar('x[%i][%i]' % (i, destino)))
    x[0].append(solver.BoolVar('x[%i][%i]' % (origem, i)))

pprint(x)


# Criando dict de cores onde a chave é a cor e o valor é uma lista de vértices
cores = {cor : [] for cor in dados.cores}

for index, cor in enumerate(dados.cores):
    cores[cor].append(index + 1)

# Criando as variáveis de vertices
y = []
for i in range(1, dados.qntVertices + 1):
    y.append(solver.BoolVar('y[%i]' % (i)))
# OK

print(cores)

# Restrição para as cores 
for key in cores.keys():
    constraint = solver.Constraint(1, float('inf'))
    for i in cores[key]:
        
        constraint.SetCoefficient(y[i - 1], 1)


for key in cores.keys():
    constraint = solver.Constraint(1, float('inf'))
    for vertice in cores[key]:
        for i in range(0, dados.qntVertices +1):
            if type(x[i][vertice-1]) != int:
                constraint.SetCoefficient(x[i][vertice-1], 1)
        

# Restrição das arestas
for i in range(1, dados.qntVertices + 1): # ASSUMIR DE 1-3
    constraint = solver.Constraint(0,0)
    for j in range(1, dados.qntVertices + 2): #ASSUMIR DE 1-4
        if j == i:
            pass
        else:
            constraint.SetCoefficient(x[i][j-1], 1)
            if j != dados.qntVertices + 1:
                constraint.SetCoefficient(x[j][i-1], -1)  ##ATUALIZANDO O J
    constraint.SetCoefficient(x[0][i-1], -1)
    constraint.SetCoefficient(x[i][destino-1], 1)

# Restrição dos vertices ficticios
constraint = solver.Constraint(1, 1)
for i in range(1, dados.qntVertices + 1):
    constraint.SetCoefficient(x[0][i-1], 1)

constraint = solver.Constraint(1, 1)
for i in range(1, dados.qntVertices + 1):
    constraint.SetCoefficient(x[i][destino-1], 1)

# Restrincão entre arestas e vertices
for i in range(0, dados.qntVertices):
    constraint = solver.Constraint(1, float("inf"))
    constraint.SetCoefficient(y[i], -1)

    for j in range(0, dados.qntVertices + 1):
        if i+1 == j:
            pass
        else:
            constraint.SetCoefficient(x[j][i], 1)
            

# Função objetivo
objective = solver.Objective()
for arco in arcos:
    #print("%i*x[%i][%i]" % (arco[2], arco[0], arco[1]))
    #print(x[arco[0]][arco[1]-1])
    objective.SetCoefficient(x[arco[0]][arco[1]-1], arco[2])

    
objective.SetMinimization()

status = solver.Solve()




if status == pywraplp.Solver.OPTIMAL:
    print('Solucao:')
    print('Valor objetivo =', solver.Objective().Value())
    print()
    """ for i in range(1, dados.qntVertices + 1):
        for j in range(1, dados.qntVertices + 1):
            if i != j and x[i][j].solution_value() > 0:
                print('x[%i][%i] = %i' % (i, j, x[i][j].solution_value())) """
    for list in x:
        for element in list:
            if type(element) != int:
                print(f"{element} = {element.solution_value()}")
    print()
    for i in range(1, dados.qntVertices + 1):
        if y[i - 1].solution_value() > 0:
            print('y[%i] = %i' % (i, y[i - 1].solution_value()))
else:
    print('O problema nao possui solucao otima.')



