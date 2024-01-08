from reader import Reader
from ortools.linear_solver import pywraplp
from pprint import pprint

solver = pywraplp.Solver.CreateSolver("SCIP")
reader = Reader("input.txt")
# DESTINO, ORIGEM, DISTANCIA
data = reader.data


n = reader.quantidadeDeArestas
x = [None]*n

#CRIANDO VARIAVEIS
for i in range(0, n):
    x[i] = solver.BoolVar(f"x{data[i][0]}{data[i][1]}")



# TENTATIVA DE CRIAR UM DICIONARIO
dic_test = {x[i].name():i for i in range(0, len(x))}
pprint(dic_test)

print(f"Numero de variaveis: {solver.NumVariables()}")

# SE TIVER SAINDO, PEGA A EQUIVALENCIA E MULTIPLICA POR 1
# SE TIVER ENTRANDO, PEGA A EQUIVALENCIA E MULTIPLICA POR -1


# CRIANDO RESTRICOES:
constraints = [None]*reader.quantidadeDeVertices
for i in range(0, reader.quantidadeDeVertices):
    if i == 0 or i == (reader.quantidadeDeVertices - 1):
        constraints[i] = solver.Constraint(1, 1, f"c{i}")

    else:
        constraints[i] = solver.Constraint(0, 0, f"c{i}")

    for array in data:
        if ( int(array[0]) - 1) == i:
            equivalencia = dic_test[f"x{array[0]}{array[1]}"]

            constraints[i].SetCoefficient(x[equivalencia], 1)
        


# CRIANDO FUNÇÃO OBJECTIVA
objective = solver.Objective()
for i in range(0, n):
    objective.SetCoefficient(x[i], int(data[i][2]))

objective.SetMinimization()


# CRIANDO RESTRIÇÕES 2.0






solver.Solve()
print("Solution: ")
print(f"Valor objetivo: {objective.Value()}")

for variable in x:
    print(f"{variable.name()} = {variable.SolutionValue()}")

# with open("test.mps", "w") as out_f:
#     mps_text = solver.ExportModelAsMpsFormat(fixed_format=False, obfuscated=False)
#     out_f.write(mps_text)


# X12 + XAC = 1
# X23 + X24 + X25 - X12 = 0
# X34 + 

