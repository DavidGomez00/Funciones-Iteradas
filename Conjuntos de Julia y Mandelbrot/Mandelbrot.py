from math import log, log2
MAX_ITER = 80

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    if n == MAX_ITER:
        return MAX_ITER
    # Retornamos esto en vez de n para poder asociar el numero de iteraciones al color
    return n + 1 - log(log2(abs(z)))
pass

if __name__ == "__main__":
    for a in range(-10, 10, 5):
        for b in range(-10, 10, 5):
            c = complex(a/10, b/10)
            print(c, mandelbrot(c))
pass
