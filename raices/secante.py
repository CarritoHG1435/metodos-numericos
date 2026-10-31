import streamlit as st
import sympy as sp
import plotly.graph_objects as go
from raices.metodos.metodo_secante import secante
from util.submit_funcs import a_lambda, iniciar_plot, configurar_slider

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

        for i, row in df.iterrows():
            visible = (i == 0)
            p0_i, p1_i, p2_i = row['p0'], row['p1'], row['p2']
            y_sec = ((f(p1_i) - f(p0_i)) / (p1_i - p0_i)) * (x - p1_i) + f(p1_i)

            fig.add_trace(go.Scatter(
                x=x,
                y=y_sec,
                mode='lines',
                name='Secante',
                line=dict(color='#00C0F2'),
                visible=visible
            ))
            fig.add_trace(go.Scatter(
                x=[p2_i],
                y=[0],
                mode='markers',
                name='Raiz',
                marker=dict(color='#FF4B4B', size=9),
                visible=visible
            ))

        configurar_slider(fig, len(df), trazas_por_iter=2)

if calcular:
    st.divider()
    col_tabla, col_grafica = st.columns([1, 1], vertical_alignment='center')
    with col_grafica:
        st.plotly_chart(fig, use_container_width=True)
    with col_tabla:
        st.dataframe(df, use_container_width=True)
