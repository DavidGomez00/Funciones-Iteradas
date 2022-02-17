from PIL import Image, ImageDraw
import numpy as np
import random

WIDTH = 600
HEIGHT = 600

def function(point):
    return  random.choice(list) @ point
pass

def normalize(n, lowerBound, upperBound, minValue, maxValue):
    range = maxValue - minValue
    newRange = upperBound - lowerBound
    return (n-minValue)/range * newRange + lowerBound
pass

if __name__ == '__main__':
    # Create image
    img = Image.new('RGB', (WIDTH, HEIGHT))
    pixels = img.load()

    # Starting point
    p = np.array([20, 20, 1]).transpose()

    # matrix
    matrix1 = np.array([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]])
    matrix2 = np.array([[0.5, 0, 0], [0, 0.5, 1], [0, 0, 1]])
    matrix3 = np.array([[0.5, 0, 1], [0, 0.5, 0], [0, 0, 1]])
    list = [matrix1, matrix2, matrix3]

    # number of points in the image
    points = 1000000

    # Run at least 40 iterations
    for i in range(40):
        p = function(p)
    pass

    # Start tracking the point
    for i in range(points):
        p = function(p)
        x = int(normalize(p[0], -300, 300, -1, 1))
        y = int(normalize(p[1], -300, 300, -1, 1))
        pixels[x, y] = 255
    pass

    # Draw image
    img.save("Triangulo_Sierpinski.png")
pass
