import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def a_lambda(text):
    sym_x = sp.Symbol('x')
    expr = sp.sympify(text)
    return sp.lambdify(sym_x, expr, 'numpy'), expr

def iniciar_plot(f, expr, resul):
    fig, ax = plt.subplots()
    x = np.linspace(-20, 20, 1000)
    y = f(x)
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#262730')
    ax.set_ylim(-15, 15)
    ax.set_xlim(-5, 5)
    ax.axhline(0, color="white", linewidth=1.2)
    ax.axvline(0, color="white", linewidth=1.2)
    ax.tick_params(colors='white', which='both')
    ax.scatter(resul, 0, label='Raiz', color='#FF4B4B')

    for spine in ax.spines.values():
        spine.set_color('white')

    ax.plot(x, y, label='f(x)', color='#FF4B4B')
    ax.set_title(f"$f(x) = {sp.latex(expr)}$", color='white')
    return fig, ax, x
