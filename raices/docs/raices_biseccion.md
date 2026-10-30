## Teorema del valor intermedio

Sea $f$ una función continua en $[a, b]$, entonces para cada valor $\alpha \in [f(a), f(b)]$ o $[f(b), f(a)]$, existe $c \in [a, b]$ tal que $f(c) = \alpha$.

![Gráfica del Teorema del Valor Intermedio](grafica_tvi.png)

## Método de Bisección

Sea $f \in C_{[a, b]}$, si $f(a) \cdot f(b) < 0$ entonces existe $c \in [a, b]$ tal que $f(c) = 0$.

Para obtener una aproximación a la raíz $c$, se obtiene el punto medio del intervalo:

$$
c = \frac{a + b}{2}
$$

La primera aproximación es $c_1$. El proceso se repite considerando el nuevo intervalo $[a, c]$ o $[c, b]$. Se toma el intervalo donde hay cambio de signo de la función evaluada en los extremos.

![Gráfica del Método de Bisección](grafica_biseccion.png)

### Cálculo de errores (a partir de las aproximaciones $c_1, c_2, c_3$)

* **Err. Abs. (Error Absoluto):**

  $$
  \vert{}c_1 - c_2\vert{}
  $$

  $$
  \vert{}c_2 - c_3\vert{}
  $$

* **Err. rel. (Error Relativo):**

  $$
  \frac{\vert{}c_1 - c_2\vert{}}{\vert{}c_2\vert{}}
  $$

  $$
  \frac{\vert{}c_2 - c_3\vert{}}{\vert{}c_3\vert{}}
  $$

### Determinar el n. de iteraciones

Partiendo de un intervalo $[a, b]$, el error máximo es:

* $\text{it } 1: \frac{b - a}{2}$

* $\text{it } 2: \frac{\frac{b - a}{2}}{2} = \frac{b - a}{2^2}$

* $\text{it } n: \frac{b - a}{2^n}$

Se desea que:

$$
\frac{b - a}{2^n} \le Err
$$

$$
\log_2\left(\frac{b - a}{Err}\right) \le n
$$

---

### ¿Cómo funcionan las iteraciones en la tabla?

Para construir una tabla de iteraciones en el método de bisección, cada fila $i$ (comenzando desde $i = 0$ o $i = 1$) sigue una secuencia lógica para reducir el intervalo a la mitad en cada paso:

1. **Definición de extremos ($a$ y $b$):** En la primera fila ($i = 0$), se colocan los extremos del intervalo inicial $[a, b]$ donde se verificó que $f(a) \cdot f(b) < 0$.
2. **Cálculo del punto medio ($c$):** Se calcula la aproximación actual promediando los extremos de esa misma fila:
   $$
   c_i = \frac{a_i + b_i}{2}
   $$
3. **Selección del nuevo intervalo para la siguiente fila ($i + 1$):** Se evalúa la función en los extremos y en el punto medio para identificar en qué mitad ocurre el cambio de signo:
   * **Caso 1:** Si $f(a_i) \cdot f(c_i) < 0$, la raíz se encuentra en la mitad izquierda $[a_i, c_i]$. Por lo tanto, para la siguiente fila se conserva $a_{i+1} = a_i$ y el extremo derecho se actualiza con $b_{i+1} = c_i$.
   * **Caso 2:** Si $f(c_i) \cdot f(b_i) < 0$, la raíz se encuentra en la mitad derecha $[c_i, b_i]$. Por lo tanto, para la siguiente fila el extremo izquierdo se actualiza con $a_{i+1} = c_i$ y se conserva $b_{i+1} = b_i$.
4. **Cálculo del error (`err`):**
   * En la iteración inicial ($i = 0$), dado que aún no existe una aproximación previa, suele registrarse la longitud inicial del intervalo $\vert{}b - a\vert{}$.
   * A partir de la siguiente iteración ($i \ge 1$), se calcula el **error relativo** comparando la aproximación actual $c_i$ con la aproximación de la fila anterior $c_{i-1}$:
     $$
     err_i = \frac{\vert{}c_i - c_{i-1}\vert{}}{\vert{}c_i\vert{}}
     $$

---

### Ejemplo de aplicación

Encontrar una aproximación a la raíz de la función:

$$
f(x) = x^3 - 5x + 2
$$

en el intervalo inicial $[a, b] = [-3, -1]$.


#### Análisis de las primeras iteraciones:

* **Verificación inicial:**
  * $f(-3) = (-3)^3 - 5(-3) + 2 = -27 + 15 + 2 = -10 < 0$
  * $f(-1) = (-1)^3 - 5(-1) + 2 = -1 + 5 + 2 = 6 > 0$
  * Como $f(-3) \cdot f(-1) < 0$, existe una raíz dentro de $[-3, -1]$.

* **Iteración $0$:**
  * Intervalo: $a = -3$, $b = -1$
  * Punto medio: $c_0 = \frac{-3 + (-1)}{2} = -2$
  * Evaluamos en la función: $f(-2) = (-2)^3 - 5(-2) + 2 = -8 + 10 + 2 = 4 > 0$
  * Como $f(-3) < 0$ y $f(-2) > 0$, el cambio de signo está en $[-3, -2]$, por lo que en la siguiente iteración $b$ toma el valor de $-2$.

* **Iteración $1$:**
  * Nuevo intervalo: $a = -3$, $b = -2$
  * Punto medio: $c_1 = \frac{-3 + (-2)}{2} = -2.5$
  * Error relativo: $err = \frac{\vert{}-2.5 - (-2)\vert{}}{\vert{}-2.5\vert{}} = \frac{0.5}{2.5} = 0.2$
  * Evaluamos en la función: $f(-2.5) = (-2.5)^3 - 5(-2.5) + 2 = -15.625 + 12.5 + 2 = -1.125 < 0$
  * Como $f(-2.5) < 0$ y $f(-2) > 0$, el cambio de signo está en $[-2.5, -2]$, por lo que en la siguiente iteración $a$ toma el valor de $-2.5$.

* **Iteración $2$:**
  * Nuevo intervalo: $a = -2.5$, $b = -2$
  * Punto medio: $c_2 = \frac{-2.5 + (-2)}{2} = -2.25$
  * Error relativo: $err = \frac{\vert{}-2.25 - (-2.5)\vert{}}{\vert{}-2.25\vert{}} = \frac{0.25}{2.25} \approx 0.1111$

#### Tabla de iteraciones

| Iteración ($i$) | $a$ | $b$ | $c$ | $err$ |
| :---: | :---: | :---: | :---: | :---: |
| $0$ | $-3$ | $-1$ | $-2$ | $2$ |
| $1$ | $-3$ | $-2$ | $-2.5$ | $0.2$ |
| $2$ | $-2.5$ | $-2$ | $-2.25$ | $0.1111$ |
| $3$ | $-2.5$ | $-2.25$ | $-2.375$ | $0.0526$ |
| $4$ | $-2.5$ | $-2.375$ | $-2.4375$ | $0.0256$ |
| $5$ | $-2.4375$ | $-2.375$ | $-2.4062$ | $0.013$ |
| $6$ | $-2.4375$ | $-2.4062$ | $-2.4219$ | $0.0065$ |
| $7$ | $-2.4219$ | $-2.4062$ | $-2.4141$ | $0.0032$ |
| $8$ | $-2.4219$ | $-2.4141$ | $-2.418$ | $0.0016$ |
| $9$ | $-2.418$ | $-2.4141$ | $-2.416$ | $0.0008$ |

Al cabo de $9$ iteraciones, obtenemos como aproximación a la raíz $c \approx -2.416$ con un error relativo de $0.0008$.
