import streamlit as st

st.set_page_config(page_title="Métodos Numéricos", layout="wide")


# 1. Defines tus vistas (pueden ser funciones o rutas a archivos .py)
def pagina_inicio():
    st.title("Bienvenido a Métodos Numéricos")
    st.write("Selecciona un método en el menú lateral para comenzar.")


def metodo_biseccion():
    st.title("Método de Bisección")


def metodo_newton():
    st.title("Método de Newton-Raphson")


def metodo_gauss():
    st.title("Eliminación de Gauss")


# 2. Organizas la navegación por secciones en el sidebar automáticamente
paginas = {
    "General": [
        st.Page(pagina_inicio, title="Inicio", icon="🏠", default=True),
    ],

    # TODO Punto flotante
    "Raíces de Ecuaciones": [
        # TODO Metodo de biseccion
        st.Page('raices/biseccion.py', title="Bisección", icon="📉"),
        # TODO Metodo de la secante
        st.Page('raices/secante.py', title="Secante", icon="📉"),
        # TODO Metodo de falsa posicion
        st.Page('raices/falsa_posicion.py', title='Falsa Posicion', icon='📉'),
        # TODO Metodo de newton-rapshon
        st.Page('raices/newton_rapshon.py', title='Newton - Rapshon', icon="📉"),
        # TODO Metodo de punto fijo
        st.Page('raices/punto-fijo.py', title='Punto Fijo', icon="📉"),
        # TODO Metodo de Muller
        st.Page('raices/muller.py', title='Muller', icon="📉"),
        # TODO Metodo de Deflacion
        st.Page('raices/deflacion.py', title='Deflacion', icon="📉"),
    ],

    "Interpolacion": [
        # TODO Metodo de Lagrange
        st.Page('interpolacion/lagrange.py', title='Lagrange', icon='〰️'),
        # TODO Metodo de Fracciones divididas
        st.Page('interpolacion/fracciones_divididas.py', title='Fracciones divididas', icon='〰️'),
        # TODO Metodo de Hermite
        st.Page('interpolacion/hermite.py', title='Hermite', icon='〰️'),
        # TODO Metodo de Neville
        st.Page('interpolacion/neville.py', title='Neville', icon='〰️'),
        # TODO Metodo de Splines Cubicos
        st.Page('interpolacion/splines.py', title='Splines Cubicos', icon='〰️'),
    ],

    "Derivacion e integracion": [
        # TODO Metodo de derivacion por 2 puntos
        st.Page('di_numerica/derivacion/2_puntos.py', title='Fórmula de 2 Puntos', icon='⚡', url_path='2-puntos'),
        # TODO Metodo de derivacion por 3 puntos
        st.Page('di_numerica/derivacion/3_puntos.py', title='Fórmula de 3 Puntos', icon='⚡', url_path='3-puntos'),
        # TODO Metodo de derivacion por 5 puntos
        st.Page('di_numerica/derivacion/5_puntos.py', title='Fórmula de 5 Puntos', icon='⚡', url_path='5-puntos'),
        # TODO Metodo de extrapolacion de richardson
        st.Page('di_numerica/derivacion/richardson.py', title='Extrapolación de Richardson', icon='⚡'),
        # TODO Metodo de integracion por regla del trapecio
        st.Page('di_numerica/integracion/trapecio.py', title='Regla del Trapecio', icon='🧱'),
        # TODO Metodo de integracion por regla de simpson 1/3
        st.Page('di_numerica/integracion/simpson13.py', title='Regla de Simpson 1/3', icon='🧱'),
        # TODO Metodo de integracion por regla de simpson 3/8
        st.Page('di_numerica/integracion/simpson38.py', title='Regla de Simpson 3/8', icon='🧱'),
        # TODO Metodo de integracion de Romberg
        st.Page('di_numerica/integracion/rombert.py', title='Método de Romberg', icon='🧱'),
        # TODO Metodo de integracion por cuadratura adaptativa
        st.Page('di_numerica/integracion/cuadratura_adaptiva.py', title='Cuadratura Adaptativa', icon='🧱'),
        # TODO Metodo de integracion por cuadratura gaussiana
        st.Page('di_numerica/integracion/cuadratura_gaussiana.py', title='Cuadratura Gaussiana', icon='🧱'),
        # TODO Metodo de integracion multiple por regla del trapecio
        st.Page('di_numerica/integracion/multiple_trapecio.py', title='Multiple Regla del Trapecio', icon='🧱'),
        # TODO Metodo de integracion multiple por regla de simpson 1/3
        st.Page('di_numerica/integracion/multiple_simpson13.py', title='Multiple Regla de Simpson 1/3', icon='🧱'),
        # TODO Metodo de integracion multiple por regla de simpson 3/8
        st.Page('di_numerica/integracion/multiple_simpson38.py', title='Multiple Regla de Simpson 3/8', icon='🧱'),
    ],
    "Sistemas de Ecuaciones": [
        st.Page(metodo_gauss, title="Eliminación de Gauss", icon="🔢"),
    ],
}

# 3. Creas el navegador y ejecutas la página seleccionada
pg = st.navigation(paginas, position="sidebar")

# Puedes seguir agregando controles globales al sidebar debajo de la navegación:
with st.sidebar:
    st.markdown('### Autores:\n'
                '- Hernandez Carrillo Hugo\n'
                '- Legaria Mendoza Fernando\n')
    st.divider()
    Decimales = st.selectbox("Decimales a mostrar", [4, 6, 8, 10], index=1)

pg.run()