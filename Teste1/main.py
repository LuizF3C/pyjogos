import pygame
from pygame.locals import *

from sys import exit

pygame.init()

largura = 640
altura = 480

x = 0
y = 0

largP = 40
altuP = 40

velP = 10

xb = 120
yb = 120

ponto = 0
fonte = pygame.font.SysFont('comic sans ms', 30, True, True)

ecra = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jooj')
ampulheta = pygame.time.Clock()

while True:
    
    ampulheta.tick(60)
    ecra.fill((0,0,0))

    mensagem= f'Colidiu {ponto}'
    texto_formatado = fonte.render(mensagem, True, (255, 10, 40))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # if event.type == KEYDOWN: 
        #     if event.key == K_d: x +=velP

        #     if event.key == K_a: x -=velP

        #     if event.key == K_w: y -=velP

        #     if event.key == K_s: y +=velP

    
    #Blocos
    player = pygame.draw.rect(ecra, (50,100,200), (x, y, largP, altuP))

    bloco = pygame.draw.rect(ecra, (80,100,0), (xb, yb, largP, altuP))

    if player.colliderect(bloco):
        xb = x + largP
        ponto += 1

    #Movimento

    if pygame.key.get_pressed()[K_a]:
        x -= velP

    if pygame.key.get_pressed()[K_d]:
        x += velP

    if pygame.key.get_pressed()[K_w]:
        y -= velP

    if pygame.key.get_pressed()[K_s]:
        y += velP

    if y > altura: y = -altuP
    if y < -altuP: y = altura
    if x > largura: x = -largP
    if x < -largP: x = largura

    ecra.blit(texto_formatado, (largura/2, 40))

    pygame.display.update()
