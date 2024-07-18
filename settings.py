import pygame
import os

# Cores definidas em RGB
BRANCO = (255, 255, 255)       # Cor branca
PRETO = (0, 0, 0)              # Cor preta
CINZAESCURO = (40, 40, 40)     # Cor cinza escuro
CINZACLARO = (100, 100, 100)  # Cor cinza claro
VERDE = (0, 255, 0)           # Cor verde
VERDEESCURO = (0, 200, 0)     # Cor verde escuro
AZUL = (0, 0, 255)            # Cor azul
VERMELHO = (255, 0, 0)        # Cor vermelha
AMARELO = (255, 255, 0)       # Cor amarela
BGCOLOR = CINZAESCURO         # Cor de fundo do jogo

# Configurações do Jogo
TAMANHOPISO = 25               # Tamanho de cada piso em pixels
LINHAS = 15                    # Número de linhas no tabuleiro
COLUNAS = 15                   # Número de colunas no tabuleiro
QUANTIDADE_MINAS = 10          # Número total de minas no tabuleiro
LARGURA = TAMANHOPISO * LINHAS # Largura total da tela
ALTURA = TAMANHOPISO * COLUNAS # Altura total da tela
FPS = 60                       # Frames por segundo
TITULO = "Campo Minado Clone"  # Título da janela do jogo

# Configurações do Temporizador
TEMPO_TOTAL = 120               # Tempo total do jogo em segundos
FONTE_TAMANHO = 20             # Tamanho da fonte do temporizador
FONTE_COR = PRETO              # Cor da fonte do temporizador
TIMER_POSICAO = (LARGURA // 16, 16) # Posição do temporizador na tela

# Função para carregar e escalar imagens
def carregar_imagem(nome_arquivo):
    # Carrega uma imagem do arquivo especificado e a escala para o tamanho do piso
    return pygame.transform.scale(pygame.image.load(os.path.join("Imagens", nome_arquivo)), (TAMANHOPISO, TAMANHOPISO))

# Carregamento das imagens dos pisos
tile_numbers = [carregar_imagem(f"Tile{i}.png") for i in range(1, 9)]  # Imagens para as dicas numeradas de 1 a 8
tile_empty = carregar_imagem("TileEmpty.png")      # Imagem para piso vazio
tile_exploded = carregar_imagem("TileExploded.png") # Imagem para piso com mina explodida
tile_flag = carregar_imagem("TileFlag.png")         # Imagem para piso com bandeira
tile_mine = carregar_imagem("TileMine.png")         # Imagem para mina
tile_unknown = carregar_imagem("TileUnknown.png")   # Imagem para piso desconhecido
tile_not_mine = carregar_imagem("TileNotMine.png")  # Imagem para piso que não é mina
