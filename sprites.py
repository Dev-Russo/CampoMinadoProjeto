import random
import pygame
from settings import *

# Lista dos tipo
# "." -> Desconhecido
# "X" -> Mina
# "C" -> Dica
# "/" -> VAzio

class Piso:
    #Construtor da classe Piso
    def __init__(self, x, y, imagem, tipo, revelado=False, bandeira=False):
        #Define as Cordenadas EX: 0-0 Canto superior, multiplicamos pelo tamanho do piso para termo9s o pixel que queremos estilizar com os sprites
        self.x, self.y = x * TAMANHOPISO, y * TAMANHOPISO
        self.imagem = imagem
        self.tipo = tipo
        self.revelado = revelado
        self.bandeira = bandeira

    def desenha(self, superfice_do_tabuleiro):
        #Verifica se o piso não é do tipo bandeira e é revelado
        if not self.bandeira and self.revelado:
            #A imagem vai ficar do jeito que ela é mesmo
            superfice_do_tabuleiro.blit(self.imagem, (self.x, self.y))
        #Verifica se é do tipo bandeira e não é revelado
        elif self.bandeira and not self.revelado:
            #A imagem vai ficar do tipo bandeira
            superfice_do_tabuleiro.blit(tile_flag, (self.x, self.y))
        #Se não estiver revelado
        elif not self.revelado:
            #A imagem fica do tipo deconhecido
            superfice_do_tabuleiro.blit(tile_unknown, (self.x, self.y))

    #Criado para fazer as representações graficas no tabuleiro, faz com que volte o tipo dos pisos e não a representação e onde esta localizado na memória
    def __repr__(self):
        return self.tipo

#Classe usada para ver o que acontece na tela
class Tabuleiro:
    def __init__(self):
        self.superfice_do_tabuleiro = pygame.Surface((ALTURA, LARGURA))
        #Permite que coloquemos os pisos no tabuleiro, Basicamente ele cria o tabuleiro do comeco do jogo onde todos os pisos são desconhecidos 
        #Usando o tamanho que já foi definido de linhas e colunas em settings.py
        self.lista_do_tabuleiro = [[Piso(colunas, linhas, tile_empty, ".") for linhas in range (LINHAS)] for colunas in range (COLUNAS)]
        self.colocando_minas()
        self.pistas()
        self.cavados = []

    def colocando_minas(self):
        for _ in range(QUANTIDADE_MINAS):
            while True:
                x = random.randint(0, LINHAS-1)
                y = random.randint(0, COLUNAS-1)

                if self.lista_do_tabuleiro[x][y].tipo == ".":
                    self.lista_do_tabuleiro[x][y].imagem = tile_mine
                    self.lista_do_tabuleiro[x][y].tipo = "X"
                    break



    def pistas(self):
        #Verifica a matriz
        for x in range(LINHAS):
            for y in range(COLUNAS):
                #Verifica se é diferente do tipo bomba
                if self.lista_do_tabuleiro[x][y].tipo != "X":
                    #Se for chama o metodo viznhos para verificar quantas bombas tem perto daquele spot
                    total_minas = self.vizinhos(x, y)
                    #Se o contador for maior que 0 adiciona a imagem number e troca tambem o tipo para C (Clue)
                    if total_minas > 0:
                        self.lista_do_tabuleiro[x][y].imagem = tile_numbers[total_minas-1]
                        self.lista_do_tabuleiro[x][y].tipo = "C"

    #Verifica se está dentro do tabuleiro
    @staticmethod
    def dentro(x, y):
        return 0 <= x < LINHAS and 0 <= y < COLUNAS


    #Verifica se há bomba por perto de cada quadrado
    def vizinhos(self, x, y):
        total_minas = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                vizinho_x = x + x_offset
                vizinho_y = y + y_offset
                #Comparação pra ver se realmente é uma bomba se for adiciona 1 ao contador
                if self.dentro(vizinho_x, vizinho_y) and self.lista_do_tabuleiro[vizinho_x][vizinho_y].tipo == "X":
                    total_minas += 1

        return total_minas



    #Desenha linha por linha do tabuleiro e começando nas coordenadas 0,0
    def desenha(self, tela):
        for linhas in self.lista_do_tabuleiro:
            for piso in linhas:
                piso.desenha(self.superfice_do_tabuleiro)
        tela.blit(self.superfice_do_tabuleiro, (0, 0))


    def cavar(self, x, y):
        #Se for do tipo mina mostra a imagem explodida e revela o spot
        self.cavados.append((x, y))
        if self.lista_do_tabuleiro[x][y].tipo == "X":
            self.lista_do_tabuleiro[x][y].revelado = True
            self.lista_do_tabuleiro[x][y].imagem = tile_exploded
            return False
        #Se for do tipo dica revela direto
        elif self.lista_do_tabuleiro[x][y].tipo == "C":
            self.lista_do_tabuleiro[x][y].revelado = True
            return True
        #Se for de qqr outro tipo ele apenas mostra
        self.lista_do_tabuleiro[x][y].revelado = True


        #Percorre a matriz dentro dos limites permitidos
        for linha in range(max(0, x-1), min(LINHAS-1, x+1) + 1):
            for coluna in range(max(0, y-1), min(COLUNAS-1, y+1) + 1):
                #Verifica se os valores já não foram processados e estão dentro da lista
                if (linha, coluna) not in self.cavados:
                    #Chama recursivamente até retornar true
                    self.cavar(linha, coluna)
        return True

    def mostrar_tabuleiro(self):
        for linhas in self.lista_do_tabuleiro:
            print(linhas)