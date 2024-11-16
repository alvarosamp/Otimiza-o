import numpy as np
from scipy.optimize import linprog

class SimplexSolver:
    
    def __init__(self, c, A, b):
        # Certifique-se de que c, A e b sejam arrays do numpy
        self.c = np.array(c, dtype=float)
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
    
    def solve(self):
       
        
        result = linprog(c=-self.c, A_ub=self.A, b_ub=self.b, method='highs')
        
        if result.success:
            solution = result.x
            optimal_value = -result.fun
            return solution, optimal_value
        else:
            return None, None
