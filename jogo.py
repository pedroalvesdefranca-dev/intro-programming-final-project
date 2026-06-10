import pygame

pygame.init()

#Definir as dimensões da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Título")

player = pygame.Rect(300, 250, 50, 50)

run = True
while run:

    screen.fill((0, 0, 0))#Tela toda Preta

    pygame.draw.rect(screen, (255, 0, 0), player)
    #Movimentação:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
