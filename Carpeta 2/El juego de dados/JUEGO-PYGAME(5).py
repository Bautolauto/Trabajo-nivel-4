
import pygame
import random

# Inicialización de Pygame
pygame.init()

 
# Dimensiones
ANCHO = 800
ALTO = 700

# Carga y escalado del fondo
FONDO = pygame.image.load("fondo/Fondo-western-para-juego.png")
FONDO = pygame.transform.scale(FONDO, (ANCHO, ALTO))

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)

# Fuente
fuente = pygame.font.SysFont(None, 40)

# Ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Dados")
reloj = pygame.time.Clock()

# Carga de imágenes de dados
imagenes_dados = [pygame.image.load(f"C:/Users/Bienvenido/Desktop/ejercicios de programacion/El juego de dados/dados/dado{i}.jpg") for i in range(1, 7)]

# Variables del juego
jugador_dados = []
cpu_dados = []
jugador_suma = 0
cpu_suma = 0
turno = "jugador"
resultado = ""

dado_animando = False
tiempo_animacion = 0
dado_random = 1

cpu_animando = False
tiempo_cpu_animacion = 0

def reiniciar_juego():
    global jugador_dados, cpu_dados, jugador_suma, cpu_suma, turno, resultado
    global dado_animando, tiempo_animacion, cpu_animando, tiempo_cpu_animacion, dado_random
    jugador_dados = []
    cpu_dados = []
    jugador_suma = 0
    cpu_suma = 0
    turno = "jugador"
    resultado = ""
    dado_animando = False
    tiempo_animacion = 0
    cpu_animando = False
    tiempo_cpu_animacion = 0
    dado_random = 1

def tirar_dado():
    return random.randint(1, 6)

def turno_jugador():
    global jugador_suma, turno, dado_animando, tiempo_animacion, dado_random, jugador_dados
    if jugador_suma < 10 and not dado_animando:
        valor = tirar_dado()
        jugador_dados.append(valor)
        jugador_suma += valor
        dado_random = valor
        dado_animando = True
        tiempo_animacion = pygame.time.get_ticks()
    if jugador_suma >= 10:
        turno = "cpu"

def turno_cpu():
    global cpu_suma, turno, cpu_animando, tiempo_cpu_animacion, dado_random, cpu_dados
    if not cpu_animando:
        if cpu_suma < 10:
            debe_tirar = False
            if cpu_suma < 6:
                debe_tirar = True
            elif cpu_suma < 9 and jugador_suma > cpu_suma:
                debe_tirar = random.choice([True, False])
            if debe_tirar:
                dado_random = tirar_dado()
                cpu_animando = True
                tiempo_cpu_animacion = pygame.time.get_ticks()
            else:
                evaluar_ronda()
        else:
            evaluar_ronda()
    else:
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_cpu_animacion >= 800:
            cpu_dados.append(dado_random)
            cpu_suma += dado_random
            cpu_animando = False
            if cpu_suma >= 10 or len(cpu_dados) >= 10:
                evaluar_ronda()

def evaluar_ronda():
    global resultado, turno
    turno = "fin"
    if jugador_suma > 10:
        resultado = "Te pasaste. ¡Perdiste!"
    elif cpu_suma > 10:
        resultado = "PEPE se pasó. ¡Ganaste!"
    elif cpu_suma > jugador_suma:
        resultado = "PEPE ganó."
    elif cpu_suma < jugador_suma:
        resultado = "¡Ganaste!"
    else:
        resultado = "Empate."

def dibujar_dado(x, y, valor, tamaño=70):
    imagen = pygame.transform.scale(imagenes_dados[valor - 1], (tamaño, tamaño))
    pantalla.blit(imagen, (x, y))

def dibujar_juego():
    pantalla.blit(FONDO, (0, 0))  # Fondo western

    # Dados jugador
    for i, valor in enumerate(jugador_dados):
        dibujar_dado(80 + i * 80, 150, valor)

    # Dados CPU
    for i, valor in enumerate(cpu_dados):
        dibujar_dado(80 + i * 80, 500, valor)

    # Animación actual
    if turno == "jugador" and dado_animando:
        dibujar_dado(ANCHO // 2 - 40, 280, dado_random, 90)
    elif turno == "cpu" and cpu_animando:
        dibujar_dado(ANCHO // 2 - 40, 530, dado_random, 90)

    # Suma
    texto_j = fuente.render(f"Jugador: {jugador_suma}", True, BLANCO)
    texto_c = fuente.render(f"CPU: {cpu_suma}", True, BLANCO)
    pantalla.blit(texto_j, (80, 80))
    pantalla.blit(texto_c, (80, 430))

    # Botones
    if turno == "jugador" and jugador_suma < 10 and not dado_animando:
        pygame.draw.rect(pantalla, VERDE, (580, 150, 180, 50))
        pantalla.blit(fuente.render("TIRAR DADO", True, BLANCO), (590, 160))
        pygame.draw.rect(pantalla, ROJO, (580, 220, 180, 50))
        pantalla.blit(fuente.render("PLANTARSE", True, BLANCO), (590, 230))

    # Resultado
    if turno == "fin":
        texto_r = fuente.render(resultado, True, BLANCO)
        pantalla.blit(texto_r, (ANCHO // 2 - texto_r.get_width() // 2, 620))

def manejar_eventos():
    global turno
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if turno == "jugador" and not dado_animando:
                if 580 <= x <= 760 and 150 <= y <= 200:
                    turno_jugador()
                elif 580 <= x <= 760 and 220 <= y <= 270:
                    turno = "cpu"
            if turno == "fin":
                reiniciar_juego()
    return True

def actualizar():
    global dado_animando, tiempo_animacion, turno
    tiempo_actual = pygame.time.get_ticks()
    if dado_animando and tiempo_actual - tiempo_animacion > 800:
        dado_animando = False
        if jugador_suma >= 10:
            turno = "cpu"
    if turno == "cpu":
        turno_cpu()

# Bucle principal
corriendo = True
while corriendo:
    corriendo = manejar_eventos()
    actualizar()
    dibujar_juego()
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()