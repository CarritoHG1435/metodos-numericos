import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
from raices.metodos.metodo_secante import secante
from util.submit_funcs import a_lambda, iniciar_plot, configurar_animacion

st.title("📉 Método de la secante")
st.markdown("Encuentra la raíz de una función continua por medio de secantes de la funcion definida inicialmente por $(p_0,f(p_0)), (p_1, f(p_1))$.")

with st.expander("📖 Ver fórmula y teoría"):
    with open('./raices/docs/secante.md', 'r', encoding='utf-8') as file:
        teoria = file.read()
    st.markdown(teoria)

tol_default = st.session_state.get("tol_global", 1e-6)
iter_default = st.session_state.get("max_iter_global", 100)

with st.form("form_secante"):
    st.subheader("Parámetros de entrada")

    funcion_str = st.text_input("Función f(x)", value="x**3 - x - 2", help="Usa sintaxis de Python, ej: x**2 - 4")

    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Valor de $p_0$", value=1.0)
    with col2:
        b = st.number_input("Valor de $p_1$", value=2.0)
    with col3:
        tolerancia = st.number_input("Tolerancia", value=tol_default, format="%.1e")

    calcular = st.form_submit_button("🚀 Calcular Raíz", use_container_width=True)

    if calcular:
        f, expr = a_lambda(funcion_str)
        df, resul = secante(f, a, b, tolerancia)
        st.markdown(f'Funcion: ${sp.latex(expr)}$')
        st.text(f'Resultado: {resul}')

        fig, x = iniciar_plot(f, expr)
        x_recta = np.array([-20.0, 20.0])

        trazas_por_iteracion = []
        for _, row in df.iterrows():
            p0_i, p1_i, p2_i = float(row['p0']), float(row['p1']), float(row['p2'])
            fp0_i, fp1_i = float(f(p0_i)), float(f(p1_i))
            y_sec = ((fp1_i - fp0_i) / (p1_i - p0_i)) * (x_recta - p1_i) + fp1_i

            trazas_por_iteracion.append([
                go.Scatter(
                    x=x_recta,
                    y=y_sec,
                    mode='lines',
                    name='Secante',
                    line=dict(color='#00C0F2', simplify=False)
                ),
                go.Scatter(
                    x=[p0_i],
                    y=[fp0_i],
                    mode='markers',
                    name='(p0, f(p0))',
                    marker=dict(color='#8038FF', size=9, symbol='circle')
                ),
                go.Scatter(
                    x=[p1_i],
                    y=[fp1_i],
                    mode='markers',
                    name='(p1, f(p1))',
                    marker=dict(color='#00F2A9', size=9, symbol='circle')
                ),
                go.Scatter(
                    x=[p2_i],
                    y=[0],
                    mode='markers',
                    name='Raiz (p2)',
                    marker=dict(color='#FF4B4B', size=9)
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
