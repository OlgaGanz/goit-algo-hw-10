from pulp import *


prob = LpProblem("Maximize production", LpMaximize)

x1 = LpVariable("Lemonade", lowBound=0, cat="Integer")       # Lemonade
x2 = LpVariable("Fruit juice", lowBound=0, cat="Integer")       # Fruit juice

prob += x1 + x2         # main

# limits
prob += 2*x1 + x2 <= 100    # water
prob += x1 <= 50            # sugar
prob += x1 <= 30            # lemon juice
prob += x2 <= 40            # fruit puree

prob.solve()

# Output results
print ("Status: ", LpStatus[prob.status])
for v in prob.variables():
    print (v.name, "=", v.varValue)
    