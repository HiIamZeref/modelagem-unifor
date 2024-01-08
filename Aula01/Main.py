from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP") # PLI == SCIP ; GLOP == PL

# CRIANDO VARIAVEIS
x = solver.IntVar(0, float("inf"), "x1")
y = solver.IntVar(0, float("inf"), "x2")
print(f"Numero de variaveis {solver.NumVariables()}")



# CRIANDO FUNÇÃO OBJETIVA
objective = solver.Objective()
objective.SetCoefficient(x, 100000)
objective.SetCoefficient(y, 200000)
objective.SetMinimization()

# CRIANDO RESTRIÇÕES
# c0 = solver.Constraint(float("-inf"), 17.5, "c0")
# c0.SetCoefficient(x, 1)
# c0.SetCoefficient(y, 7)

# c1 = solver.Constraint(float("-inf"), 3.5, "c1")
# c1.SetCoefficient(x, 1)
# c1.SetCoefficient(y, 0)


solver.Add(8 * x + 2 * y >= 16)
solver.Add(x + y >= 6)
solver.Add(2 * x + 7 * y >= 28)



solver.Solve()
print("Solution: ")
print(f"Objective value =  {objective.Value()}")
print("x =", x.solution_value())
print("y =", y.solution_value())
