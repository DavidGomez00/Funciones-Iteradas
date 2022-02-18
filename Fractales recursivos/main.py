import turtle
import random

# Ventana 
window = turtle.Screen()
# Color del fondo
window.bgcolor("black")

# Creo la tortuga
tortuga = turtle.Turtle()
# Velocidad de la tortuga
tortuga.speed(80)
tortuga.left(90)

def dibujaArbol(rama, tortuga):
    ''' Dibuja el fractal básico.
    '''

    # condicion de salida
    if (rama < 5):
        return
    tortuga.forward(rama)
    tortuga.left(45)

    # dibuja subarbol de la izquierda
    dibujaArbol((rama*0.5), tortuga)

    # dibuja el árbol de la derecha
    tortuga.right(90)

    # dibujo el subarbol de la derecha
    dibujaArbol((rama*0.5), tortuga)

    # vuelvo a la posición inicial
    tortuga.left(45)
    tortuga.backward(rama)

def dibujaArbolRealistaRandom(rama, tortuga):
    ''' Anñade parámetros random al fractral para
    generar un árbol "realista".
    '''

    # Grosor del lápiz
    tortuga.pensize(rama/10)

    # condicion de salida
    if (rama < 40):
        return
    tortuga.forward(rama)
    tortuga.left(30)

    # dibuja subarbol de la izquierda
    dibujaArbolRealistaRandom((rama*random.uniform(0.8, 0.9)), tortuga)

    # ajusto para dibujar el árbol de la derecha
    tortuga.right(60)

    # dibujo el subarbol de la derecha
    dibujaArbolRealistaRandom((rama*random.uniform(0.8, 0.9)), tortuga)

    # vuelvo a la posición inicial
    tortuga.left(30)
    tortuga.backward(rama)

# posicion inicial
tortuga.penup()
tortuga.setpos(0, -100)
tortuga.pendown()

# Dibuja los árboles
tortuga.color("white")
dibujaArbol(200, tortuga)
#dibujaArbolRealistaRandom(100, tortuga)

# exit program
window.exitonclick()
