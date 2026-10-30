# Método de la secante

Este método considera que contamos con dos aproximaciones, $p_0$ y $p_1$ a la raíz de una función continua $f(x)$.

En este método se obtiene la recta que pasa por $(p_0, f_0)$ y $(p_1, f_1)$ y se calcula la intersección de esta recta con el eje $x$. Esta intersección $p_2$, es la nueva aproximación a la raíz.

![Gráfica del Método de la Secante](grafica_secante.png)

El proceso se repite considerando a $p_1$ y $p_2$ como nuevos puntos iniciales.

$$
E_{abs} = \vert{}p_2 - p_1\vert{} = \vert{}p_{n+1} - p_n\vert{}
$$

## Cálculo de $p_2$

$$
m = \frac{f_1 - f_0}{p_1 - p_0} \rightarrow m = \frac{y - f_1}{x - p_1}
$$

Igualando ambas pendientes (Ec. de la recta $L$):

$$
\frac{y - f_1}{x - p_1} = \frac{f_1 - f_0}{p_1 - p_0}
$$

Despejando $y$:

$$
y = \frac{f_1 - f_0}{p_1 - p_0}(x - p_1) + f_1
$$

Obtención de la intersección de $L$ con el eje $x$ (Sea $y = 0$):

$$
\frac{f_1 - f_0}{p_1 - p_0}(x - p_1) + f_1 = 0
$$

Despejando $x$:

$$
(x - p_1) = -f_1 \frac{(p_1 - p_0)}{f_1 - f_0}
$$

$$
x = p_2 = p_1 - f_1 \left( \frac{p_1 - p_0}{f_1 - f_0} \right)
$$

---

## ¿Cómo funcionan las iteraciones en la tabla?

A diferencia del método de bisección (donde se verifica el cambio de signo para decidir qué extremo conservar), el método de la secante es un **método abierto** y su tabla se actualiza mediante un desplazamiento directo de los puntos en cada fila $i$:

1. **Puntos iniciales ($p_0$ y $p_1$):** En la primera fila ($i = 0$), se colocan las dos aproximaciones iniciales propuestas $p_0$ y $p_1$ (no necesitan encerrar la raíz).
2. **Cálculo de la nueva aproximación ($p_2$):** Se evalúa la función en ambos puntos ($f_0 = f(p_0)$ y $f_1 = f(p_1)$) y se aplica la fórmula de la secante para hallar la intersección con el eje $x$:

   $$
   p_2 = p_1 - f(p_1) \left( \frac{p_1 - p_0}{f(p_1) - f(p_0)} \right)
   $$

3. **Actualización para la siguiente fila ($i + 1$):** Sin importar los signos, los valores siempre se recorren una posición hacia la izquierda para continuar el proceso:
   * El antiguo $p_1$ pasa a ser el nuevo $p_0$ ($p_{0,\text{nuevo}} = p_{1,\text{anterior}}$).
   * El recién calculado $p_2$ pasa a ser el nuevo $p_1$ ($p_{1,\text{nuevo}} = p_{2,\text{anterior}}$).
4. **Criterio de paro:** El proceso se repite hasta que el error absoluto $\vert{}p_2 - p_1\vert{}$ (o relativo) sea menor que la tolerancia deseada.

---

## Ejemplo de aplicación

Encontrar una aproximación a la raíz de la función:

$$
f(x) = x^3 - 5x + 2
$$

utilizando los puntos iniciales $p_0 = 0$ y $p_1 = 3$.

![Ejemplo del Método de la Secante](ejemplo_secante.png)

### Análisis de las primeras iteraciones:

* **Iteración $0$:**
  * Puntos actuales: $p_0 = 0$, $p_1 = 3$
  * Evaluamos en la función:
    * $f(0) = (0)^3 - 5(0) + 2 = 2$
    * $f(3) = (3)^3 - 5(3) + 2 = 27 - 15 + 2 = 14$
  * Calculamos $p_2$:

    $$
    p_2 = 3 - 14 \left( \frac{3 - 0}{14 - 2} \right) = 3 - 14 \left( \frac{3}{12} \right) = 3 - 3.5 = -0.5
    $$

* **Iteración $1$:**
  * Recorremos los puntos: $p_0 = 3$, $p_1 = -0.5$
  * Evaluamos en la función:
    * $f(3) = 14$
    * $f(-0.5) = (-0.5)^3 - 5(-0.5) + 2 = -0.125 + 2.5 + 2 = 4.375$
  * Calculamos $p_2$:

    $$
    p_2 = -0.5 - 4.375 \left( \frac{-0.5 - 3}{4.375 - 14} \right) = -0.5 - 4.375 \left( \frac{-3.5}{-9.625} \right) \approx -2.0909
    $$

* **Iteración $2$:**
  * Recorremos los puntos: $p_0 = -0.5$, $p_1 = -2.0909$
  * Evaluamos en la función:
    * $f(-0.5) = 4.375$
    * $f(-2.0909) = (-2.0909)^3 - 5(-2.0909) + 2 \approx -9.1411 + 10.4545 + 2 = 3.3134$
  * Calculamos $p_2$:

    $$
    p_2 = -2.0909 - 3.3134 \left( \frac{-2.0909 - (-0.5)}{3.3134 - 4.375} \right) \approx -7.0557
    $$

### Tabla de iteraciones

| Iteración ($i$) | $p_0$ | $p_1$ | $p_2$ |
| :--- | :--- | :--- | :--- |
| $0$ | $0$ | $3$ | $-0.5$ |
| $1$ | $3$ | $-0.5$ | $-2.0909$ |
| $2$ | $-0.5$ | $-2.0909$ | $-7.0557$ |
| $3$ | $-2.0909$ | $-7.0557$ | $-2.1428$ |
| $4$ | $-7.0557$ | $-2.1428$ | $-2.1873$ |
| $5$ | $-2.1428$ | $-2.1873$ | $-2.46$ |
| $6$ | $-2.1873$ | $-2.46$ | $-2.4077$ |
| $7$ | $-2.46$ | $-2.4077$ | $-2.414$ |

**Resultado final:** Tras $7$ iteraciones, se obtiene la aproximación a la raíz $p \approx -2.414042510640844$.