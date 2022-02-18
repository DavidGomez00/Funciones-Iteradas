import turtle

# window
win = turtle.Screen()
win.bgcolor("black")

# turtle
tortuga = turtle.Turtle()
tortuga.speed(0)

# settings
g_angle = 90
g_forward = 5
g_iterations = 4

# posicion inicial
tortuga.penup()
tortuga.setpos(-625, 100)
tortuga.pendown()
tortuga.color("white")

# sentencia inicial
sentencia = 'F'

def itera(sentencia):
    ''' Aplica las reglas de la gramática a la sentencia
    de forma iterativa.
    '''

    for _ in range(g_iterations):
        # Nueva sentencia
        nueva_sentencia = ''
        # Recorre la sentencia
        for caracter in sentencia:
            aux = ''
            # aplica las reglas
            if(caracter == 'F'):
                aux = 'F+F-F-F+F'
                nueva_sentencia += aux
            elif (caracter == '-'):
                nueva_sentencia += '-'
            elif (caracter == '+'):
                nueva_sentencia += '+'
        sentencia = nueva_sentencia

    return sentencia

def translate(sentencia_final):
    ''' Traduce la sentencia dada a instrucciones de turtle
    para generar el sistema.
    '''

    for caracter in sentencia_final:
        if(caracter == 'F'): tortuga.forward(g_forward)
        elif(caracter == '+'): tortuga.right(g_angle)
        elif(caracter == '-'): tortuga.left(g_angle)

# Ejecuta el programa
sentencia_final = itera(sentencia)
translate(sentencia_final)

# exit program
win.exitonclick()
