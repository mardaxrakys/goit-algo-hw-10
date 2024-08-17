import pulp

# Створення моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішення
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
juice = pulp.LpVariable("Juice", lowBound=0, cat='Continuous')

# Цільова функція: максимізація загальної кількості продуктів
model += lemonade + juice, "Total_Production"

# Обмеження
model += 2 * lemonade + 1 * juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Статус розв'язку:", pulp.LpStatus[model.status])
print("Кількість Лимонаду для виробництва:", lemonade.varValue)
print("Кількість Фруктового соку для виробництва:", juice.varValue)
print("Максимальна загальна кількість продуктів:", pulp.value(model.objective))
