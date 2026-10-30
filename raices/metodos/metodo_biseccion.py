import numpy as np
import pandas as pd

def biseccion(a, b, f, err, max_iter = 100):
    vec_a = [a]
    vec_b = [b]
    vec_c = [(a+b)/2]
    vec_err = [abs((b-a)/b)]

    iteracion = 0
    while vec_err[-1] > err and iteracion < max_iter:
        if f(vec_a[-1]) * f(vec_c[-1]) < 0:
            vec_a.append(vec_a[-1])
            vec_b.append(vec_c[-1])
        elif f(vec_b[-1]) * f(vec_c[-1]) < 0:
            vec_a.append(vec_c[-1])
            vec_b.append(vec_b[-1])
        else:
            raise Exception("Debe de haber diferencia de signos entre a y b")

        nuevo_c = (vec_a[-1] + vec_b[-1])/2
        vec_c.append(nuevo_c)

        if nuevo_c != 0:
            vec_err.append(abs((nuevo_c - vec_c[-2]) / nuevo_c))
        else:
            vec_err.append(abs(nuevo_c - vec_c[-2]))
        iteracion += 1

    print(len(vec_a), len(vec_b), len(vec_c), len(vec_err))

    data = {
        "a": np.array(vec_a),
        "b": np.array(vec_b),
        "c": np.array(vec_c),
        "err": np.array(vec_err)
    }

    df = pd.DataFrame(data)
    resul = df['c'].iloc[-1]

    return (df, resul)
