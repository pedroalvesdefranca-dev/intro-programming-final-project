import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

posicao_x = 20
posicao_y = 480

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Título")

#Imagens do cenário
BACKGROUND_INICIAL = pygame.image.load("cin-pixel.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_INICIAL, (SCREEN_WIDTH, SCREEN_HEIGHT-100))
GROUND_INICIAL = pygame.image.load("ground.png")
GROUND = pygame.transform.scale(GROUND_INICIAL, (SCREEN_WIDTH, SCREEN_HEIGHT-500))

#Imagens do personagem
FIGURA_PARADA = pygame.transform.scale(pygame.image.load("parado.png"), (96, 112)).convert_alpha()
FIGURA_PULANDO = pygame.transform.scale(pygame.image.load("pulo.png"), (96, 112)).convert_alpha()
FIGURA_CORRENDO = pygame.transform.scale(pygame.image.load("correndo.png"), (96, 112)).convert_alpha()
FIGURA_ATACANDO = pygame.transform.scale(pygame.image.load("atacando.png"), (96, 112)).convert_alpha()

player = FIGURA_PARADA.get_rect(center=(posicao_x, posicao_y))

movimento = False
ataque = False
pulando = False
Y_GRAVIDADE = 1
ALTURA_PULO = 18
Y_VELOCIDADE = ALTURA_PULO

rodando = True
while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            sys.exit()

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(GROUND, (0, 500))

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        pulando = True
    elif key[pygame.K_a]:
        player.move_ip(-5, 0)
        movimento = True
    elif key[pygame.K_d]:
        player.move_ip(5, 0)
        movimento = True
    elif key[pygame.K_x]:
        ataque = True
    if pulando:
        player.y -= Y_VELOCIDADE
        Y_VELOCIDADE -= Y_GRAVIDADE
        if Y_VELOCIDADE < -ALTURA_PULO:
            pulando = False
            Y_VELOCIDADE = ALTURA_PULO
        screen.blit(FIGURA_PULANDO, player)
    else:
        if movimento:
            screen.blit(FIGURA_CORRENDO, player)
        elif ataque:
            screen.blit(FIGURA_ATACANDO, player)
        else:
            screen.blit(FIGURA_PARADA, player)

    movimento = False
    ataque = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
