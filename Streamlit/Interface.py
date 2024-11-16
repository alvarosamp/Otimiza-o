import streamlit as st
from Simplex import SimplexSolver
def main():
    
    st.title("Resolução de Programação Linear usando o Método Simplex")
    st.write("Desenvolvido para o trabalho prático de M210")

    
    st.header("Configuração da Função Objetivo")
    num_vars = st.number_input("Número de variáveis", min_value=2, max_value=4, value=2)

    c = []
    for i in range(num_vars):
        coef = st.number_input(f"Coeficiente x{i + 1}", value=1.0)
        c.append(coef)
    
    
    st.header("Configuração das Restrições")
    num_constraints = st.number_input("Número de restrições", min_value=1, max_value=4, value=2)
    
    A = []
    b = []
    for j in range(num_constraints):
        st.subheader(f"Restrição {j + 1}")
        row = []
        for i in range(num_vars):
            coef = st.number_input(f"Coeficiente x{i + 1} para restrição {j + 1}", value=1.0)
            row.append(coef)
        A.append(row)
        rhs = st.number_input(f"Valor à direita da restrição {j + 1} (≤)", value=10.0)
        b.append(rhs)

    if st.button("Resolver"):
        # Criar uma instância da classe SimplexSolver
        solver = SimplexSolver(c, A, b)
        solution, optimal_value = solver.solve()
        
        if solution is not None:
            st.success("Solução ótima encontrada!")
            st.write("Valores das variáveis:")
            for i, val in enumerate(solution):
                st.write(f"x{i + 1} = {val:.2f}")
            st.write(f"Valor ótimo da função objetivo: {optimal_value:.2f}")
        else:
            st.error("Não foi possível encontrar uma solução viável.")

    # 
    st.write("---")

if __name__ == "__main__":
    main()