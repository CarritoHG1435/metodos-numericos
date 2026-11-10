import streamlit as st
import sympy as sp
import plotly.graph_objects as go
from raices.metodos.metodo_biseccion import biseccion
from util.submit_funcs import a_lambda, iniciar_plot, configurar_animacion

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
        df, resul = biseccion(a, b, f, tolerancia, max_iter=max_iter)
        st.markdown(f'Funcion: ${sp.latex(expr)}$')
        st.text(f'Resultado: {resul}')

        fig, x = iniciar_plot(f, expr)

        trazas_por_iteracion = []
        for _, row in df.iterrows():
            trazas_por_iteracion.append([
                go.Scatter(
                    x=[row['a'], row['a']],
                    y=[-20, 20],
                    mode='lines',
                    name='a',
                    line=dict(color='#00C0F2', simplify=False)
                ),
                go.Scatter(
                    x=[row['b'], row['b']],
                    y=[-20, 20],
                    mode='lines',
                    name='b',
                    line=dict(color='#8038FF', simplify=False)
                ),
                go.Scatter(
                    x=[row['c']],
                    y=[0],
                    mode='markers',
                    name='Raiz (c)',
                    maker=dict(color='#FF4B4B', size=9)
                )
            ])

        configurar_animacion(fig, trazas_por_iteracion)

if calcular:
    st.divider()
    col_tabla, col_grafica = st.columns([0.6, 1.4], vertical_alignment='center')
    with col_grafica:
        st.plotly_chart(fig, use_container_width=True)
    with col_tabla:
        st.dataframe(df, use_container_width=True)
