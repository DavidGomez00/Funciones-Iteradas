from PIL import Image, ImageDraw
from Mandelbrot import mandelbrot, MAX_ITER

# Tamaño de la imagen
WIDTH = 600
HEIGHT = 400

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

# Image
image = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(image)

# For each pixel
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Convierte las coordenadas del pixel a un número
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START), IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Calcula el número de iteraciones
        iteraciones = mandelbrot(c)
        # El color depende del número de iteraciones
        h = int(255*iteraciones/MAX_ITER)
        saturacion = 255
        value = 255 if iteraciones < MAX_ITER else 0
        # Plot the point
        draw.point([x, y], (h, saturacion, value))

# Save image
image.convert('RGB').save('Mandelbrot.png', 'PNG')
