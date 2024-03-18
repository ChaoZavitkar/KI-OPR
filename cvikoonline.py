import pulp

# Definovat proměnné
x = pulp.LpVariable("x", 0, None, pulp.LpInteger)
y = pulp.LpVariable("y", 0, None, pulp.LpInteger)
z = pulp.LpVariable("z", 0, None, pulp.LpInteger)

# Definovat účelovou funkci
obj = pulp.LpProblem("Zisk", pulp.LpMaximize)
obj.setObjective(2 * x + 2 * y + 4 * z)

# Definovat omezení
obj.addConstraint(2 * x + y + z <= 2)
obj.addConstraint(3 * x + 4 * y + 2 * z >= 8)

# Vyřešit problém
obj.solve()

# Vytisknout řešení
print(obj.status)
print(obj.objective)
print(x.value())
print(y.value())
print(z.value())
