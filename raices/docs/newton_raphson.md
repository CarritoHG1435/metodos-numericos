# Método de Newton-Raphson

El **Método de Newton-Raphson** es un algoritmo iterativo perteneciente al análisis numérico, utilizado para encontrar aproximaciones a las raíces o ceros de una función real de variable real (es decir, valores de $x$ tales que $f(x) = 0$).

---

## 1. ¿De qué trata el método?

A grandes rasgos, el método se basa en una aproximación lineal local mediante el cálculo diferencial:

1. Se parte de una estimación inicial de la raíz, denotada como $p_0$.
2. En el punto $(p_0, f(p_0))$, se traza la **recta tangente** a la curva de la función $f(x)$.
3. Se determina el punto donde esta recta tangente interseca al eje $x$ (es decir, donde $y = 0$).
4. Dicho punto de intersección se define como la nueva aproximación $p_1$, la cual, bajo condiciones favorables, estará mucho más cerca de la raíz verdadera que $p_0$.
5. El procedimiento se repite cíclicamente ($p_1 \to p_2 \to p_3 \to \dots \to p_{i+1}$) hasta que la diferencia entre iteraciones consecutivas sea menor o igual a una tolerancia o error preestablecido.

---

## 2. Requisitos para poder concretarse

Para aplicar el método de forma válida y garantizar su convergencia, se deben satisfacer las siguientes condiciones:

1. **Continuidad y diferenciabilidad:** La función $f(x)$ debe ser continua y diferenciable (al menos $C^1$) en el intervalo que contiene a la raíz y a las aproximaciones sucesivas.
2. **Aproximación inicial adecuada ($p_0$):** Se requiere un valor inicial suficientemente próximo a la raíz buscada para evitar problemas de divergencia, oscilaciones o convergencia a otra raíz no deseada.
3. **Derivada no nula en cada punto de prueba:** En ninguna iteración la derivada puede ser cero ($f'(p_i) \neq 0$). Si la derivada se anula, la recta tangente es horizontal ($m = 0$) y nunca intersectará al eje $x$ (provocando una división entre cero en la fórmula).
4. **Criterio de paro definido:** Se debe establecer una tolerancia máxima permitida de error para detener el algoritmo, comúnmente evaluada con:
   - **Error absoluto:**
     $$|p_{i+1} - p_i| \le \text{Error}$$
   - **Error relativo:**
     $$\left| \frac{p_{i+1} - p_i}{p_{i+1}} \right| \le \text{Error}$$

---

## 3. Demostración matemática del método

La deducción de la fórmula iterativa proviene de la ecuación geométrica de una recta en el plano cartesiano.

### Paso 1: Pendiente de la recta tangente
Sea $\mathcal{L}$ la recta tangente a la curva $y = f(x)$ en el punto $(p_0, f(p_0))$. Por definición de derivada, la pendiente $m_{\mathcal{L}}$ es:
$$m_{\mathcal{L}} = f'(p_0)$$

### Paso 2: Ecuación punto-pendiente
La ecuación de la recta que pasa por $(p_0, f(p_0))$ con pendiente $m$ es:
$$\frac{y - f(p_0)}{x - p_0} = m_{\mathcal{L}}$$

Despejando $y$:
$$y = m(x - p_0) + f(p_0)$$

### Paso 3: Intersección con el eje $x$
La nueva aproximación $p_1$ corresponde al punto donde la recta interseca el eje horizontal, es decir, cuando $y = 0$ y $x = p_1$:
$$0 = m(p_1 - p_0) + f(p_0)$$

Despejamos el término que contiene a $p_1$:
$$m(p_1 - p_0) = -f(p_0)$$

$$p_1 - p_0 = -\frac{f(p_0)}{m}$$

$$p_1 = p_0 - \frac{f(p_0)}{m}$$

### Paso 4: Sustitución de la pendiente
Sustituyendo $m = f'(p_0)$:
$$p_1 = p_0 - \frac{f(p_0)}{f'(p_0)}$$

### Fórmula general iterativa
Generalizando para cualquier iteración $i$:
$$p_{i+1} = p_i - \frac{f(p_i)}{f'(p_i)}$$

---

## 4. Cómo llenar la tabla de iteraciones

La tabla organiza el cálculo paso a paso y consta habitualmente de 6 columnas:

| $i$ | $p_i$ | $f(p_i)$ | $f'(p_i)$ | $p_{i+1}$ | $\text{Error}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Col. 1 | Col. 2 | Col. 3 | Col. 4 | Col. 5 | Col. 6 |

### Instrucciones de llenado por columnas:

1. **Columna 1 ($i$):** Registra el índice o número de iteración ($1, 2, 3, \dots$).
2. **Columna 2 ($p_i$):**
   - Para la primera fila ($i = 1$), se coloca el valor inicial propuesto $p_0$.
   - Para las filas siguientes ($i > 1$), se traslada el resultado obtenido en la columna $p_{i+1}$ de la fila anterior.
3. **Columna 3 ($f(p_i)$):** Se evalúa la función original sustituyendo el valor actual $p_i$.
4. **Columna 4 ($f'(p_i)$):** Se evalúa la derivada de la función sustituyendo el valor actual $p_i$.
5. **Columna 5 ($p_{i+1}$):** Se calcula la nueva aproximación aplicando la fórmula:
   $$p_{i+1} = p_i - \frac{f(p_i)}{f'(p_i)}$$
6. **Columna 6 ($\text{Error}$):** Se evalúa la discrepancia entre el valor nuevo y el anterior. Se calcula como:
   $$\text{Error} = \left| \frac{p_{i+1} - p_i}{p_{i+1}} \right| \quad \text{o} \quad \text{Error} = |p_{i+1} - p_i|$$
7. **Condición de término:** Si el valor de la columna $\text{Error} \le \text{Tolerancia}$, el proceso se detiene y $p_{i+1}$ es la aproximación final. Si no se cumple, se abre una nueva fila.

---

## 5. Ejemplo desarrollado

**Problema:** Obtener una aproximación a $\sqrt[3]{2}$ con un error máximo de $1 \times 10^{-3}$ usando Newton-Raphson.

### Modelado matemático
1. Planteamiento de la ecuación:
   $$x = \sqrt[3]{2} \implies x^3 = 2 \implies f(x) = x^3 - 2 = 0$$
2. Derivada de la función:
   $$f'(x) = 3x^2$$
3. Parámetros iniciales:
   - Valor inicial: $p_0 = 1.5$
   - Tolerancia / Error máximo: $1 \times 10^{-3} = 0.001$

---

### Cálculos detallados

#### Iteración 1 ($i = 1$):
- $p_1 = 1.5$
- $f(1.5) = (1.5)^3 - 2 = 3.375 - 2 = 1.375$
- $f'(1.5) = 3(1.5)^2 = 3(2.25) = 6.75$
- $p_2 = 1.5 - \frac{1.375}{6.75} = 1.5 - 0.203703... \approx 1.296296$
- $\text{Error relativo} = \left| \frac{1.296296 - 1.5}{1.296296} \right| \approx 0.1571 \approx 0.16$ (No cumple: $0.16 > 0.001$).

#### Iteración 2 ($i = 2$):
- $p_2 = 1.296296$
- $f(1.296296) = (1.296296)^3 - 2 \approx 0.178216$
- $f'(1.296296) = 3(1.296296)^2 \approx 5.041152$
- $p_3 = 1.296296 - \frac{0.178216}{5.041152} \approx 1.260932$
- $\text{Error relativo} = \left| \frac{1.260932 - 1.296296}{1.260932} \right| \approx 0.02804$ (No cumple: $0.02804 > 0.001$).

#### Iteración 3 ($i = 3$):
- $p_3 = 1.260932$
- $f(1.260932) = (1.260932)^3 - 2 \approx 0.004732$
- $f'(1.260932) = 3(1.260932)^2 \approx 4.769848$
- $p_4 = 1.260932 - \frac{0.004732}{4.769848} \approx 1.259922$
- $\text{Error relativo} = \left| \frac{1.259922 - 1.260932}{1.259922} \right| \approx 0.000802$
- Como $0.000802 \le 0.001$, **el criterio de paro se satisface**.

---

### Tabla de iteraciones final

| $i$ | $p_i$ | $f(p_i)$ | $f'(p_i)$ | $p_{i+1}$ | $\text{Error (relativo)}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1.500000$ | $1.375000$ | $6.750000$ | $1.296296$ | $0.15714$ |
| $2$ | $1.296296$ | $0.178216$ | $5.041152$ | $1.260932$ | $0.02804$ |
| $3$ | $1.260932$ | $0.004732$ | $4.769848$ | $1.259922$ | $0.00080$ |

**Resultado final:** La aproximación para $\sqrt[3]{2}$ con un error menor a $1 \times 10^{-3}$ es:
$$x \approx 1.259922$$