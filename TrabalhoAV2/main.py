from reader import Reader
from ortools.linear_solver import pywraplp
from pprint import pprint

reader = Reader("balanceado.txt")
solver = pywraplp.Solver.CreateSolver("SCIP")

data = reader.data

quantidadeDestinos = reader.quantidadeDeDestinos
quantidadeOrigem = reader.quantidadeDeOrigens

producoes = reader.producoes
demandas = reader.demandas

caso = reader.caso
print(caso)

if caso == "Balanceado":
    pass # FAZ NADA
elif caso == "Desbalanceado Produção.": # PRODUÇÃO < DEMANDA
    quantidadeOrigem += 1
    
elif caso == "Desbalanceado Demanda.": # PRODUÇÃO > DEMANDA
    quantidadeDestinos += 1
    

# Inicializando a matrix de variaveis
x = [ [solver.IntVar(0, float("inf"), f"x{j+1}{i+1}") for i in range(quantidadeDestinos)]  for j in range(quantidadeOrigem)] #ORIGEM = LINHA, DESTINO = COLUNA

# Criando restrições
# Restricao origens
for i in range(0, quantidadeOrigem):
    if i == (quantidadeOrigem - 1) and caso == "Desbalanceado Produção.":
        restante = (reader.somaDemanda - reader.somaProducao)

        constraint = solver.Constraint(restante, restante, f"Origem {i+1}")
    else:
        constraint = solver.Constraint(producoes[i], producoes[i], f"Origem {i+1}")

    for j in range(0, quantidadeDestinos):
        constraint.SetCoefficient(x[i][j], 1)

# Restricao destinos
for i in range(0, quantidadeDestinos):
    if i == (quantidadeDestinos - 1) and caso == "Desbalanceado Demanda.":
        restante = (reader.somaProducao - reader.somaDemanda)
        constraint = solver.Constraint(restante, restante, f"Destino {i+1}")
    else:
        constraint = solver.Constraint(demandas[i], demandas[i], f"Destino {i+1}")

    for j in range(0, quantidadeOrigem):
        constraint.SetCoefficient(x[j][i], 1)

print(f"Numero de restricoes: {solver.NumConstraints()}")

if caso == "Balanceado":
    pass # FAZ NADA
elif caso == "Desbalanceado Produção.": # PRODUÇÃO < DEMANDA
    quantidadeOrigem -= 1
    
elif caso == "Desbalanceado Demanda.": # PRODUÇÃO > DEMANDA
    quantidadeDestinos -= 1
    

# Criando função objetiva
objective = solver.Objective()
for i in range(0, quantidadeOrigem):
    for j in range(0, quantidadeDestinos):
        objective.SetCoefficient(x[i][j], data[i][j])

objective.SetMinimization()

pprint(x)

solver.Solve()
print("Solution: ")
print(f"Valor objetivo: {objective.Value()}")

for array in x:
    for element in array:
        print(f"{element.name()} = {element.SolutionValue()}")

# for index, array in enumerate(x):
#     for index, element in enumerate(array):
#         print(f"Origem: {index}; Destino: {index}; Resultado: {element.SolutionValue()}")

