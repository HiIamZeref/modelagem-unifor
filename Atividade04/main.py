from reader import Reader
from ortools.linear_solver import pywraplp

reader = Reader("dados.txt")
solver = pywraplp.Solver.CreateSolver("SCIP")

data = reader.data

n = reader.quantidadeDePontos
x = [None] * n

#CRIANDO VARIAVEIS
for i in range(0, n):
    x[i] = solver.BoolVar(f"x{i}")

print(f"Numero de variaveis {solver.NumVariables()}")


# CRIANDO RESTRICOES
for i in range(0, reader.quantidadeDeRuas):
    constraint = solver.Constraint(1, float("Inf"), data[i][0])

    constraint.SetCoefficient(x[int(data[i][1]) - 1], 1)
    constraint.SetCoefficient(x[int(data[i][2]) - 1], 1)

print(f"Numero de restricoes: {solver.NumConstraints()}")

#CRIANDO FUNCAO OBJETIVA
objective = solver.Objective()
for variable in x:
    objective.SetCoefficient(variable, 1)

objective.SetMinimization()

solver.Solve()
print("Solution: ")
print(f"Valor objetivo: {objective.Value()}")

for variable in x:
    print(f"{variable.name()} = {variable.SolutionValue()}")

