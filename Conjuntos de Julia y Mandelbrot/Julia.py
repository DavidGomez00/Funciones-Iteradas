from math import log, log2

# Maximum of iterations
MAX_ITER = 80

def julia(c, z0):
    ''' Gets the number of iterations needed for
    each pixel.
    '''

    # Parameters
    z = z0
    n = 0

    # Iterarte julia function
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    if n == MAX_ITER:
        return MAX_ITER

    # Complex operation for colouring
    return n + 1 - log(log2(abs(z)))

if __name__ == '__main__':
    pass