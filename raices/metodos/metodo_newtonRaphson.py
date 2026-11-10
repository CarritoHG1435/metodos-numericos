import pandas as pd

def newton_raphson(f, dfx, x0, err, max_iter = 100):
    vec_p0 = [x0]
    vec_p1 = [x0 - (f(x0) / dfx(x0))]
    vec_err = [abs((vec_p1[-1] - vec_p0[-1]) / vec_p1[-1])]
    

    i = 0
    while vec_err[-1] > err and i < max_iter:
        vec_p0.append(vec_p1[-1])
        xi = vec_p1[-1]

        dfxi = dfx(xi)

        if dfxi == 0:
            break
        vec_p1.append(xi - (f(xi) / dfxi))
        vec_err.append(abs((vec_p1[-1] - vec_p0[-1]) / vec_p1[-1]))
        i+=0

    data = {
        'p0': vec_p0,
        'p1': vec_p1,
        'err': vec_err,
    }

    df = pd.DataFrame(data)
    resul = df['p1'].iloc[-1]
    return df, resul
