import numpy as np
import streamlit as st
import sympy as sp
import plotly.graph_objects as go
from fontTools.diff import color
from numpy.ma.core import size

from raices.metodos.metodo_newtonRaphson import newton_raphson
from util.submit_funcs import a_lambda, iniciar_plot, configurar_animacion

st.title("ƒ'(x) Método de Newton - Rapshon")
st.markdown("Encuentra una raiz de una funcion continua y derivable en un intervalo $[a,b]$")

with st.expander('📖 Ver fórmula y teoría'):
    with open('./raices/docs/newton_raphson.md', 'r',encoding='utf-8') as f:
        data = f.read()
    st.markdown(data)

with st.form("form_newton"):
    st.subheader("Parámetros de entrada")

    funcion_str = st.text_input("Función f(x)", value="x**3 - x - 2", help="Usa sintaxis de Python, ej: x**2 - 4")


    tol_default = st.session_state.get("tol_global", 1e-6)
    iter_default = st.session_state.get("max_iter_global", 100)


    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Punto inicial (a)", value=1.0)
    with col2:
        tolerancia = st.number_input("Tolerancia", value=tol_default, format="%.1e")
    with col3:
        max_iter = st.number_input("Máx. iteraciones", value=iter_default, min_value=1, step=10)

    calcular = st.form_submit_button("🚀 Calcular Raíz", use_container_width=True)
    if calcular:
        f, expr = a_lambda(funcion_str)
        dxf = expr.diff()
        dxf, _ = a_lambda(dxf)
        df, resul = newton_raphson(f,dxf, a,  tolerancia, max_iter=max_iter)
        st.markdown(f'Funcion: ${sp.latex(expr)}$')
        st.text(f'Resultado: {resul}')

        fig, x = iniciar_plot(f, expr)

        x_recta = np.array([-20,20])
        trazas_por_iteracion = []
        for _, row in df.iterrows():
            p0_i, p1_i = float(row['p0']), float(row['p1'])
            fi, dfi = float(f(row['p0'])), float(dxf(row['p0']))
            y_new_rec = dfi * (x_recta - p0_i) + fi
            trazas_por_iteracion.append([
                go.Scatter(
                    x=x_recta,
                    y=y_new_rec,
                    mode='lines',
                    name='Recta tangente',
                    line=dict(color='#00C0F2', simplify=False)
                ),
                go.Scatter(
                    x=[row['p0']],
                    y=[f(row['p0'])],
                    mode='markers',
                    name='Punto inicial (Pi)',
                    marker=dict(color='#FF4B4B', size=9)
                ),

                go.Scatter(
                    x=[row['p1']],
                    y=[0],
                    mode='markers',
                    name='Aprox (Pi+1)',
                    marker=dict(color='#FA1111', size=9)
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