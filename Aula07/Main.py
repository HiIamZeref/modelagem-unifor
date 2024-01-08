from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP") # PLI == SCIP ; GLOP == PL

# CRIANDO VARIAVEIS
x11 = solver.BoolVar("x11")
x12 = solver.BoolVar("x12")
x13 = solver.BoolVar("x13")
x14 = solver.BoolVar("x14")



x21 = solver.BoolVar("x21")
x22 = solver.BoolVar("x22")
x23 = solver.BoolVar("x23")
x24 = solver.BoolVar("x24")


x31 = solver.BoolVar("x31")
x32 = solver.BoolVar("x32")
x33 = solver.BoolVar("x33")
x34 = solver.BoolVar("x34")

print(f"Numero de variaveis {solver.NumVariables()}")



# CRIANDO FUNÇÃO OBJETIVA
objective = solver.Objective()
objective.SetCoefficient(x11, 7)
objective.SetCoefficient(x12, 13)
objective.SetCoefficient(x13, 12)
objective.SetCoefficient(x14, 14)

objective.SetCoefficient(x21, 15)
objective.SetCoefficient(x22, 10)
objective.SetCoefficient(x23, 16)
objective.SetCoefficient(x24, 8)

objective.SetCoefficient(x31, 21)
objective.SetCoefficient(x32, 15)
objective.SetCoefficient(x33, 28)
objective.SetCoefficient(x34, 5)
objective.SetMinimization()

# CRIANDO RESTRIÇÕES
c0 = solver.Constraint(1, 1, "c0")
c0.SetCoefficient(x11, 1)
c0.SetCoefficient(x12, 1)
c0.SetCoefficient(x13, 1)
c0.SetCoefficient(x14, 1)

c1 = solver.Constraint(1, 1, "c1")
c1.SetCoefficient(x21, 1)
c1.SetCoefficient(x22, 1)
c1.SetCoefficient(x23, 1)
c1.SetCoefficient(x24, 1)

c2 = solver.Constraint(1, 1, "c2")
c2.SetCoefficient(x31, 1)
c2.SetCoefficient(x32, 1)
c2.SetCoefficient(x33, 1)
c2.SetCoefficient(x34, 1)

c3 = solver.Constraint(0, 1, "c3")
c3.SetCoefficient(x11, 1)
c3.SetCoefficient(x21, 1)
c3.SetCoefficient(x31, 1)

c4 = solver.Constraint(0, 1, "c4")
c4.SetCoefficient(x12, 1)
c4.SetCoefficient(x22, 1)
c4.SetCoefficient(x32, 1)

c5 = solver.Constraint(0, 1, "c5")
c5.SetCoefficient(x13, 1)
c5.SetCoefficient(x23, 1)
c5.SetCoefficient(x33, 1)


c6 = solver.Constraint(0, 1, "c6")
c6.SetCoefficient(x14, 1)
c6.SetCoefficient(x24, 1)
c6.SetCoefficient(x34, 1)

# c1 = solver.Constraint(float("-inf"), 3.5, "c1")
# c1.SetCoefficient(x, 1)
# c1.SetCoefficient(y, 0)


# solver.Add(8 * x + 2 * y >= 16)
# solver.Add(x + y >= 6)
# solver.Add(2 * x + 7 * y >= 28)



solver.Solve()
print("Solution: ")
print(f"Objective value =  {objective.Value()}")

print("x11 =", x11.solution_value())
print("x12 =", x12.solution_value())
print("x13 =", x13.solution_value())
print("x14 =", x14.solution_value())

print("x21 =", x21.solution_value())
print("x22 =", x22.solution_value())
print("x23 =", x23.solution_value())
print("x24 =", x24.solution_value())

print("x31 =", x31.solution_value())
print("x32 =", x32.solution_value())
print("x33 =", x33.solution_value())
print("x34 =", x34.solution_value())


