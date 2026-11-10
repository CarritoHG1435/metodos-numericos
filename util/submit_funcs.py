import re
import sympy as sp
import numpy as np
import plotly.graph_objects as go


def a_lambda(text):
    sym_x = sp.Symbol('x')
    expr = sp.sympify(text)
    return sp.lambdify(sym_x, expr, 'numpy'), expr


def expr_a_html(expr):
    """Convierte una expresión de SymPy a HTML compatible con el título nativo de Plotly."""
    texto = sp.latex(expr)
    texto = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', texto)
    texto = re.sub(r'\^([a-zA-Z0-9])', r'<sup>\1</sup>', texto)
    texto = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', texto)
    texto = re.sub(r'_([a-zA-Z0-9])', r'<sub>\1</sub>', texto)
    texto = texto.replace(r'\cdot', '·').replace(r'\left(', '(').replace(r'\right)', ')')
    texto = texto.replace('\\', '')
    return f"<i>f(x) = {texto}</i>"


def iniciar_plot(f, expr):
    x = np.linspace(-20, 20, 10000)
    y = f(x)

    fig = go.Figure()

    # Traza 0: f(x) (siempre fija de fondo)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='f(x)',
        line=dict(color='#FF4B4B', width=2)
    ))

    fig.update_layout(
        title=dict(
            text=expr_a_html(expr),
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
        margin=dict(l=40, r=40, t=60, b=60)
    )

    return fig, x


def configurar_animacion(fig, lista_trazas_por_iter):
    """
    Recibe la figura base (con f(x) en la traza 0) y una lista donde cada elemento
    es la lista de trazas (go.Scatter) correspondientes a la iteración i.
    Configura las trazas iniciales, los frames y los controles de animación (Play/Pausa + Slider).
    """
    if not lista_trazas_por_iter:
        return

    # 1. Agregamos las trazas de la iteración 0 a la figura inicial
    for traza in lista_trazas_por_iter[0]:
        fig.add_trace(traza)

    # Índices de las trazas dinámicas (todas excepto la 0 que es f(x))
    num_dinamicas = len(lista_trazas_por_iter[0])
    indices_dinamicos = list(range(1, 1 + num_dinamicas))

    # 2. Creamos los frames para cada iteración
    frames = [
        go.Frame(
            data=trazas_iter,
            traces=indices_dinamicos,
            name=str(i)
        )
        for i, trazas_iter in enumerate(lista_trazas_por_iter)
    ]
    fig.frames = frames

    # 3. Configuramos los pasos del slider con transición suave
    pasos = [
        dict(
            method="animate",
            args=[
                [str(i)],
                dict(
                    mode="immediate",
                    frame=dict(duration=500, redraw=False),
                    transition=dict(duration=400, easing="cubic-in-out")
                )
            ],
            label=str(i)
        )
        for i in range(len(lista_trazas_por_iter))
    ]

    # 4. Agregamos botones Play/Pausa y Slider con el mismo diseño oscuro
    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            x=0.0,
            y=-0.18,
            xanchor="left",
            yanchor="top",
            direction="left",
            pad=dict(r=10, t=20),
            bgcolor="#262730",
            bordercolor="white",
            borderwidth=1,
            font=dict(color="white"),
            buttons=[
                dict(
                    label="▶ Play",
                    method="animate",
                    args=[
                        None,
                        dict(
                            fromcurrent=True,
                            frame=dict(duration=700, redraw=False),
                            transition=dict(duration=450, easing="cubic-in-out")
                        )
                    ]
                ),
                dict(
                    label="⏸ Pausa",
                    method="animate",
                    args=[
                        [None],
                        dict(
                            mode="immediate",
                            frame=dict(duration=0, redraw=False),
                            transition=dict(duration=0)
                        )
                    ]
                )
            ]
        )],
        sliders=[dict(
            active=0,
            x=0.22,
            len=0.78,
            y=-0.18,
            xanchor="left",
            yanchor="top",
            currentvalue=dict(prefix="Iteración: ", font=dict(color="white")),
            pad=dict(t=15, b=10),
            steps=pasos,
            bgcolor="#262730",
            bordercolor="white",
            font=dict(color="white"),
            activebgcolor="#FF4B4B"
        )]
    )
