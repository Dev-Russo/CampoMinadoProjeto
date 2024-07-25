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
        self._x, self._y = x * TAMANHOPISO, y * TAMANHOPISO  # Converte coordenadas do tabuleiro para pixels
        self._imagem = imagem  # Imagem associada ao piso
        self._tipo = tipo  # Tipo do piso (mina, vazio, dica, etc.)
        self._revelado = revelado  # Indica se o piso foi revelado
        self._bandeira = bandeira  # Indica se o piso tem uma bandeira

    @property
    def get_x(self):
        return self._x

    @get_x.setter
    def set_x(self, value):
        self._x = value

    @property
    def get_y(self):
        return self._y

    @get_y.setter
    def set_y(self, value):
        self._y = value

    @property
    def get_imagem(self):
        return self._imagem

    @get_imagem.setter
    def set_imagem(self, value):
        self._imagem = value

    @property
    def get_tipo(self):
        return self._tipo

    @get_tipo.setter
    def set_tipo(self, value):
        self._tipo = value

    @property
    def get_revelado(self):
        return self._revelado

    @get_revelado.setter
    def set_revelado(self, value):
        self._revelado = value

    @property
    def get_bandeira(self):
        return self._bandeira

    @get_bandeira.setter
    def set_bandeira(self, value):
        self._bandeira = value

    def desenha(self, superfice_do_tabuleiro):
        # Desenha o piso na superfície fornecida com base no seu estado
        if not self.get_bandeira and self.get_revelado:
            # Se o piso não tem bandeira e está revelado, desenha a imagem correspondente
            superfice_do_tabuleiro.blit(self.get_imagem, (self.get_x, self.get_y))
        elif self.get_bandeira and not self.get_revelado:
            # Se o piso tem bandeira e não está revelado, desenha a imagem da bandeira
            superfice_do_tabuleiro.blit(tile_flag, (self.get_x, self.get_y))
        elif not self.get_revelado:
            # Se o piso não está revelado, desenha a imagem de desconhecido
            superfice_do_tabuleiro.blit(tile_unknown, (self.get_x, self.get_y))

    def __repr__(self):
        # Retorna uma representação textual do tipo do piso
        return self.get_tipo

# Classe representando o tabuleiro do jogo
class Tabuleiro:
    def __init__(self):
        # Inicializa o tabuleiro com uma superfície e cria a grade de pisos
        self._superfice_do_tabuleiro = pygame.Surface((ALTURA, LARGURA))  # Superfície para desenhar o tabuleiro
        self._lista_do_tabuleiro = [[Piso(colunas, linhas, tile_empty, ".") for linhas in range(LINHAS)] for colunas in range(COLUNAS)]
        self.colocando_minas()  # Coloca as minas no tabuleiro
        self.pistas()  # Adiciona pistas aos pisos
        self._cavados = []  # Lista para acompanhar os pisos cavados

    @property
    def get_superfice_do_tabuleiro(self):
        return self._superfice_do_tabuleiro

    @get_superfice_do_tabuleiro.setter
    def set_superfice_do_tabuleiro(self, value):
        self._superfice_do_tabuleiro = value

    @property
    def get_lista_do_tabuleiro(self):
        return self._lista_do_tabuleiro

    @get_lista_do_tabuleiro.setter
    def set_lista_do_tabuleiro(self, value):
        self._lista_do_tabuleiro = value

    @property
    def get_cavados(self):
        return self._cavados

    @get_cavados.setter
    def set_cavados(self, value):
        self._cavados = value

    def colocando_minas(self):
        # Coloca as minas aleatoriamente no tabuleiro
        for _ in range(QUANTIDADE_MINAS):
            while True:
                x = random.randint(0, LINHAS - 1)
                y = random.randint(0, COLUNAS - 1)
                if self.get_lista_do_tabuleiro[x][y].get_tipo == ".":
                    # Se o piso escolhido é vazio, coloca uma mina nele
                    self.get_lista_do_tabuleiro[x][y].set_imagem = tile_mine
                    self.get_lista_do_tabuleiro[x][y].set_tipo = "X"
                    break

    def pistas(self):
        # Adiciona dicas ao tabuleiro com base no número de minas vizinhas
        for x in range(LINHAS):
            for y in range(COLUNAS):
                if self.get_lista_do_tabuleiro[x][y].get_tipo != "X":
                    # Se o piso não é uma mina, calcula o número de minas vizinhas
                    total_minas = self.vizinhos(x, y)
                    if total_minas > 0:
                        # Se há minas vizinhas, define a imagem de pista correspondente
                        self.get_lista_do_tabuleiro[x][y].set_imagem = tile_numbers[total_minas - 1]
                        self.get_lista_do_tabuleiro[x][y].set_tipo = "C"

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
                if self.dentro(vizinho_x, vizinho_y) and self.get_lista_do_tabuleiro[vizinho_x][vizinho_y].get_tipo == "X":
                    # Se o vizinho é uma mina, incrementa o contador
                    total_minas += 1
        return total_minas

    def desenha(self, tela):
        # Desenha todos os pisos do tabuleiro na tela
        for linhas in self.get_lista_do_tabuleiro:
            for piso in linhas:
                piso.desenha(self.get_superfice_do_tabuleiro)
        tela.blit(self.get_superfice_do_tabuleiro, (0, 0))  # Desenha o tabuleiro na tela

    def cavar(self, x, y):
        # Cava o piso nas coordenadas (x, y) e revela seu conteúdo
        self.get_cavados.append((x, y))  # Adiciona o piso à lista de cavados
        if self.get_lista_do_tabuleiro[x][y].get_tipo == "X":
            # Se o piso é uma mina, revela a mina e atualiza a imagem
            self.get_lista_do_tabuleiro[x][y].set_revelado = True
            self.get_lista_do_tabuleiro[x][y].set_imagem = tile_exploded
            return False
        elif self.get_lista_do_tabuleiro[x][y].get_tipo == "C":
            # Se o piso é uma dica, revela o piso
            self.get_lista_do_tabuleiro[x][y].set_revelado = True
            return True
        # Revela o piso e cava seus vizinhos se necessário
        self.get_lista_do_tabuleiro[x][y].set_revelado = True
        for linha in range(max(0, x - 1), min(LINHAS - 1, x + 1) + 1):
            for coluna in range(max(0, y - 1), min(COLUNAS - 1, y + 1) + 1):
                if (linha, coluna) not in self.get_cavados:
                    self.cavar(linha, coluna)
        return True

    def mostrar_tabuleiro(self):
        # Exibe o tabuleiro no console (para fins de depuração)
        for linhas in self.get_lista_do_tabuleiro:
            print(linhas)
