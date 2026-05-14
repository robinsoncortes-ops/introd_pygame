# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

# importamos la libreria pygame
import pygame
import sys
import math

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((1000,700))

# establecer titulo de la ventana
pygame.display.set_caption("dibujar formas basicas")

# definición colores
Negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255,162,0)
rosado = (255,192,203)
verde = (0,255,0)
gris = ( 128,128,128)
amarillo = (255,255,0)
blanco = (255,255,255)
cian = (0, 255, 255)

# variable auxiliarespi
pi = math.pi

# Objeto para la gestión del tiempo
clock = pygame.time.Clock()


# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        # Al hacer click sobre el boton de cerrar la ventana el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(Negro)

    # Rectangulo
    pygame.draw.rect(ventana,rojo, (150,150,50,50))
    pygame.draw.rect(ventana,naranja,(200,150,50,50))
    pygame.draw.rect(ventana,verde,(300,500,80,80))

    # linea recta 
    pygame.draw.line(ventana,gris,(300,500),(170,200),20)
    pygame.draw.line(ventana,cian,(700,500),(700,100),15)
    pygame.draw.line(ventana,cian,(500,300),(900,300),15)
    pygame.draw.line(ventana,cian,(830,450),(580,170),15)
    pygame.draw.line(ventana,cian,(840,160),(570,450),15)
    
    # carro 
    pygame.draw.rect(ventana,amarillo,(280,350,30,80))

    # circulo
    pygame.draw.circle(ventana,blanco,(700,300),200,20)

    # Rectangulo sin relleno
    pygame.draw.rect(ventana, azul, ((200,200), (50,50)), 30)
    pygame.draw.rect(ventana, rosado, ((150,200), (50,50)),30)

    # actualizar visualización de la ventana
    pygame.display.flip()