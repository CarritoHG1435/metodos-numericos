import sympy as sp
import numpy as np
import plotly.graph_objects as go


def a_lambda(text):
    sym_x = sp.Symbol('x')
    expr = sp.sympify(text)
    return sp.lambdify(sym_x, expr, 'numpy'), expr


def iniciar_plot(f, expr):
    x = np.linspace(-20, 20, 1000)
    y = f(x)

    fig = go.Figure()

    # Traza 0: f(x) (siempre visible en todas las iteraciones)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='f(x)',
        line=dict(color='#FF4B4B', width=2)
    ))

    fig.update_layout(
        title=dict(
            text=f"$f(x) = {sp.latex(expr)}$",
            font=dict(color='white', size=18),
            x=0.5,
            xanchor='center'
        ),
        paper_bgcolor='#0e1117',
        plot_bgcolor='#262730',
        font=dict(color='white'),
        xaxis=dict(
            range=[-5, 5],
            showgrid=False,
            zeroline=True,
            zerolinecolor='white',
            zerolinewidth=1.2,
            showline=True,
            linecolor='white',
            linewidth=1,
            mirror=True,
            ticks='outside',
            tickcolor='white',
            tickfont=dict(color='white')
        ),
        yaxis=dict(
            range=[-15, 15],
            showgrid=False,
            zeroline=True,
            zerolinecolor='white',
            zerolinewidth=1.2,
            showline=True,
            linecolor='white',
            linewidth=1,
            mirror=True,
            ticks='outside',
            tickcolor='white',
            tickfont=dict(color='white')
        ),
        legend=dict(
            bgcolor='rgba(38, 39, 48, 0.8)',
            bordercolor='white',
            borderwidth=1,
            font=dict(color='white')
        ),
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig, x


def configurar_slider(fig, num_iteraciones, trazas_por_iter):
    pasos = []
    total_trazas = 1 + num_iteraciones * trazas_por_iter

    for i in range(num_iteraciones):
        visibilidad = [False] * total_trazas
        visibilidad[0] = True  # Mantiene f(x) siempre visible
        inicio = 1 + i * trazas_por_iter
        for j in range(trazas_por_iter):
            visibilidad[inicio + j] = True

        pasos.append(dict(
            method="update",
            args=[{"visible": visibilidad}],
            label=str(i)
        ))

    fig.update_layout(
        sliders=[dict(
            active=0,
            currentvalue=dict(prefix="Iteración: ", font=dict(color="white")),
            pad=dict(t=30),
            steps=pasos,
            bgcolor="#262730",
            bordercolor="white",
            font=dict(color="white"),
            activebgcolor="#FF4B4B"
        )]
    )
