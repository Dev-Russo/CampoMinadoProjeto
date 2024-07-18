# Cores (r, g, b)
import pygame
import os


BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZAESCURO = (40, 40, 40)
CINZACLARO = (100, 100, 100)
VERDE = (0, 255, 0)
VERDEESCURO = (0, 200, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
BGCOLOR = CINZAESCURO


#Config do Jogo
TAMANHOPISO = 25
LINHAS = 15
COLUNAS = 15
QUANTIDADE_MINAS = 1
LARGURA = TAMANHOPISO * LINHAS
ALTURA = TAMANHOPISO * COLUNAS
FPS = 60
TITULO = "Campo Minado Clone"

#Função que faz com que as imagens fiquem de acordo com o tamanho definido posteriormente em TAMANHOPISO ou seja 32x32
#E asssim colocando essas imagens dentro da lista criada
tile_numbers = []
for i in range(1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Imagens", f"Tile{i}.png")), (TAMANHOPISO, TAMANHOPISO)))

#Transformando todas as outras imagens na escala 32x32
tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("Imagens", "TileEmpty.png")), (TAMANHOPISO, TAMANHOPISO))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("Imagens", "TileExploded.png")), (TAMANHOPISO, TAMANHOPISO))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("Imagens", "TileFlag.png")), (TAMANHOPISO, TAMANHOPISO))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("Imagens", "TileMine.png")), (TAMANHOPISO, TAMANHOPISO))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("Imagens", "TileUnknown.png")), (TAMANHOPISO, TAMANHOPISO))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("Imagens", "TileNotMine.png")), (TAMANHOPISO, TAMANHOPISO))