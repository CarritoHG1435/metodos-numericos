import streamlit as st
import streamlit as st

st.set_page_config(page_title="Métodos Numéricos", layout="wide")


# 1. Defines tus vistas (pueden ser funciones o rutas a archivos .py)
def pagina_inicio():
    st.title("Bienvenido a Métodos Numéricos")
    st.write("Selecciona un método en el menú lateral para comenzar.")


def metodo_biseccion():
    st.title("Método de Bisección")
    # Aquí va la lógica o interfaz del método


def metodo_newton():
    st.title("Método de Newton-Raphson")


def metodo_gauss():
    st.title("Eliminación de Gauss")


# 2. Organizas la navegación por secciones en el sidebar automáticamente
paginas = {
    "General": [
        st.Page(pagina_inicio, title="Inicio", icon="🏠", default=True),
    ],
    "Raíces de Ecuaciones": [
        st.Page('raices/biseccion.py', title="Bisección", icon="📉"),
        st.Page('raices/secante.py', title="Secante", icon="⚡"),
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