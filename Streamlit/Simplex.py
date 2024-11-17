import pulp

class SimplexSolver:
    def __init__(self, c, A, b):
        self.c = c
        self.A = A
        self.b = b
        self.initial_b = b[:]  # Armazena os valores iniciais de b

    def solve(self):
        # Definir o problema de maximização
        problem = pulp.LpProblem("Problema_Simplex", pulp.LpMaximize)

        # Criar variáveis de decisão
        num_vars = len(self.c)
        vars = [pulp.LpVariable(f"x{i+1}", lowBound=0) for i in range(num_vars)]

        # Definir a função objetivo
        problem += pulp.lpDot(self.c, vars), "Função Objetivo"

        # Adicionar as restrições
        for i in range(len(self.A)):
            problem += (pulp.lpDot(self.A[i], vars) <= self.b[i]), f"Restrição_{i+1}"

        # Resolver o problema usando o método Simplex
        problem.solve()

        # Obter os valores das variáveis e o valor ótimo
        solution = [v.varValue for v in vars]
        optimal_value = pulp.value(problem.objective)

        # Extrair os preços-sombra (dual values)
        shadow_prices = [constraint.pi for name, constraint in problem.constraints.items()]

        return solution, optimal_value, shadow_prices

    def calculate_profit_change(self, shadow_prices, new_b):
        """
        Calcula o impacto no lucro considerando os novos valores das restrições.
        Usa os preços-sombra para calcular o impacto no lucro.
        """
        delta_b = [new_b[i] - self.initial_b[i] for i in range(len(new_b))]
        profit_change = sum(shadow_prices[i] * delta_b[i] for i in range(len(delta_b)))
        return profit_change
