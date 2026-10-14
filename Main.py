import pygame
from Classes import *

pygame.init()

LARGURA = 1920
ALTURA = 1080
TELA = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)

pygame.display.set_caption("Lost in pixels")
cor = {"azul-claro" : (100,150,255), "amarelo" : (255,255,0), "verde" : (0,255,0)}


player = Entidade()
player.info(50, 50, 100, 910, 2, 4, 0, 40)
player_img = pygame.image.load("Imagens/mario.webp").convert_alpha()
player_img = pygame.transform.scale(player_img,(player.l, player.h))
player_fis = pygame.Rect(player.x, player.y, player.l, player.h)
player_pulo = player.pulo

chao = Plataforma()
chao.info(LARGURA, 120, 0, ALTURA - 120)
chao_fis = pygame.Rect(chao.x, chao.y, chao.l, chao.h)


rodando = True
clock = pygame.time.Clock()


i = False
c = 0
while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    TELA.fill(cor["azul-claro"])

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        player.x -= player.veloc
    if teclas[pygame.K_d]:
        player.x += player.veloc
    if (teclas[pygame .K_w] or teclas[pygame.K_UP]) and player.y >= ALTURA - chao.h - player.h:
        i = True
    if i:
        player_pulo = player_pulo - player.grav
        player.y -= player_pulo
        if player_pulo <= (-player.grav):
            i = False
            player_pulo = player.pulo
    if player.y < ALTURA - chao.h - player.h:
        player.y += player.grav

    pygame.draw.rect(TELA, cor["verde"], chao_fis)
    TELA.blit(player_img, (player.x, player.y))
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()