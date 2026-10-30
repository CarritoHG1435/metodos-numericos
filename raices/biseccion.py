import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from raices.metodos.metodo_biseccion import biseccion
from util.submit_funcs import a_lambda, iniciar_plot

st.title("📉 Método de Bisección")
st.markdown("Encuentra la raíz de una función continua en un intervalo $[a, b]$ donde $f(a) \cdot f(b) < 0$.")

with st.expander("📖 Ver fórmula y teoría"):
    with open('./raices/docs/raices_biseccion.md', 'r', encoding='utf-8') as file:
        teoria = file.read()
    st.markdown(teoria)

tol_default = st.session_state.get("tol_global", 1e-6)
iter_default = st.session_state.get("max_iter_global", 100)

with st.form("form_biseccion"):
    st.subheader("Parámetros de entrada")

    funcion_str = st.text_input("Función f(x)", value="x**3 - x - 2", help="Usa sintaxis de Python, ej: x**2 - 4")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        a = st.number_input("Límite inferior (a)", value=1.0)
    with col2:
        b = st.number_input("Límite superior (b)", value=2.0)
    with col3:
        tolerancia = st.number_input("Tolerancia", value=tol_default, format="%.1e")
    with col4:
        max_iter = st.number_input("Máx. iteraciones", value=iter_default, min_value=1, step=10)

    calcular = st.form_submit_button("🚀 Calcular Raíz", use_container_width=True)
    if calcular:
        f, expr = a_lambda(funcion_str)
        df, resul = biseccion(a,b,f,tolerancia, max_iter=max_iter)
        st.markdown(f'Funcion: ${sp.latex(expr)}$')
        st.text(f'Resultado: {resul}')


        fig, ax, x = iniciar_plot(f, expr, resul)

        ax.plot(np.full(len(x), a), x, label='a', color='#00C0F2')
        ax.plot(np.full(len(x), b), x, label='b', color='#8038FF')

        ax.legend()
        fig_height = fig.get_figheight()
        plt.close(fig)
if calcular:
    st.divider()
    col_tabla, col_grafica = st.columns([1,1], vertical_alignment='center')
    with col_grafica:
        st.pyplot(fig)
    with col_tabla:
        st.dataframe(df)