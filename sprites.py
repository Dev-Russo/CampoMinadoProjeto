import random
import pygame
from settings import *

# Lista dos tipo
# "." -> Desconhecido
# "X" -> Mina
# "C" -> Dica
# "/" -> VAzio

# Classe representando um piso do tabuleiro
class Piso:
    def __init__(self, x, y, imagem, tipo, revelado=False, bandeira=False):
        # Inicializa o piso com suas coordenadas, imagem, tipo, e status de revelado e bandeira
        self.x, self.y = x * TAMANHOPISO, y * TAMANHOPISO  # Converte coordenadas do tabuleiro para pixels
        self.imagem = imagem  # Imagem associada ao piso
        self.tipo = tipo  # Tipo do piso (mina, vazio, dica, etc.)
        self.revelado = revelado  # Indica se o piso foi revelado
        self.bandeira = bandeira  # Indica se o piso tem uma bandeira

    def desenha(self, superfice_do_tabuleiro):
        # Desenha o piso na superfície fornecida com base no seu estado
        if not self.bandeira and self.revelado:
            # Se o piso não tem bandeira e está revelado, desenha a imagem correspondente
            superfice_do_tabuleiro.blit(self.imagem, (self.x, self.y))
        elif self.bandeira and not self.revelado:
            # Se o piso tem bandeira e não está revelado, desenha a imagem da bandeira
            superfice_do_tabuleiro.blit(tile_flag, (self.x, self.y))
        elif not self.revelado:
            # Se o piso não está revelado, desenha a imagem de desconhecido
            superfice_do_tabuleiro.blit(tile_unknown, (self.x, self.y))

    def __repr__(self):
        # Retorna uma representação textual do tipo do piso
        return self.tipo

# Classe representando o tabuleiro do jogo
class Tabuleiro:
    def __init__(self):
        # Inicializa o tabuleiro com uma superfície e cria a grade de pisos
        self.superfice_do_tabuleiro = pygame.Surface((ALTURA, LARGURA))  # Superfície para desenhar o tabuleiro
        self.lista_do_tabuleiro = [[Piso(colunas, linhas, tile_empty, ".") for linhas in range(LINHAS)] for colunas in range(COLUNAS)]
        self.colocando_minas()  # Coloca as minas no tabuleiro
        self.pistas()  # Adiciona pistas aos pisos
        self.cavados = []  # Lista para acompanhar os pisos cavados

    def colocando_minas(self):
        # Coloca as minas aleatoriamente no tabuleiro
        for _ in range(QUANTIDADE_MINAS):
            while True:
                x = random.randint(0, LINHAS - 1)
                y = random.randint(0, COLUNAS - 1)
                if self.lista_do_tabuleiro[x][y].tipo == ".":
                    # Se o piso escolhido é vazio, coloca uma mina nele
                    self.lista_do_tabuleiro[x][y].imagem = tile_mine
                    self.lista_do_tabuleiro[x][y].tipo = "X"
                    break

    def pistas(self):
        # Adiciona dicas ao tabuleiro com base no número de minas vizinhas
        for x in range(LINHAS):
            for y in range(COLUNAS):
                if self.lista_do_tabuleiro[x][y].tipo != "X":
                    # Se o piso não é uma mina, calcula o número de minas vizinhas
                    total_minas = self.vizinhos(x, y)
                    if total_minas > 0:
                        # Se há minas vizinhas, define a imagem de pista correspondente
                        self.lista_do_tabuleiro[x][y].imagem = tile_numbers[total_minas - 1]
                        self.lista_do_tabuleiro[x][y].tipo = "C"

    @staticmethod
    def dentro(x, y):
        # Verifica se as coordenadas (x, y) estão dentro dos limites do tabuleiro
        return 0 <= x < LINHAS and 0 <= y < COLUNAS

    def vizinhos(self, x, y):
        # Conta o número de minas vizinhas ao piso (x, y)
        total_minas = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                vizinho_x = x + x_offset
                vizinho_y = y + y_offset
                if self.dentro(vizinho_x, vizinho_y) and self.lista_do_tabuleiro[vizinho_x][vizinho_y].tipo == "X":
                    # Se o vizinho é uma mina, incrementa o contador
                    total_minas += 1
        return total_minas

    def desenha(self, tela):
        # Desenha todos os pisos do tabuleiro na tela
        for linhas in self.lista_do_tabuleiro:
            for piso in linhas:
                piso.desenha(self.superfice_do_tabuleiro)
        tela.blit(self.superfice_do_tabuleiro, (0, 0))  # Desenha o tabuleiro na tela

    def cavar(self, x, y):
        # Cava o piso nas coordenadas (x, y) e revela seu conteúdo
        self.cavados.append((x, y))  # Adiciona o piso à lista de cavados
        if self.lista_do_tabuleiro[x][y].tipo == "X":
            # Se o piso é uma mina, revela a mina e atualiza a imagem
            self.lista_do_tabuleiro[x][y].revelado = True
            self.lista_do_tabuleiro[x][y].imagem = tile_exploded
            return False
        elif self.lista_do_tabuleiro[x][y].tipo == "C":
            # Se o piso é uma dica, revela o piso
            self.lista_do_tabuleiro[x][y].revelado = True
            return True
        # Revela o piso e cava seus vizinhos se necessário
        self.lista_do_tabuleiro[x][y].revelado = True
        for linha in range(max(0, x - 1), min(LINHAS - 1, x + 1) + 1):
            for coluna in range(max(0, y - 1), min(COLUNAS - 1, y + 1) + 1):
                if (linha, coluna) not in self.cavados:
                    self.cavar(linha, coluna)
        return True

    def mostrar_tabuleiro(self):
        # Exibe o tabuleiro no console (para fins de depuração)
        for linhas in self.lista_do_tabuleiro:
            print(linhas)
