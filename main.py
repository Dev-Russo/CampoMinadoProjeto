import pygame
from settings import *
from sprites import *


class Jogo:
    def __init__(self):
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()

    def novo(self):
        self.board = Tabuleiro()
        self.board.mostrar_tabuleiro()

    def rodar(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.eventos()
            self.desenhar()
        else:
            self.end_screen()

    
    def desenhar(self):
        self.screen.fill(BGCOLOR)
        self.board.desenha(self.screen)
        pygame.display.flip()


    def check_vitoria(self):
        for row in self.board.lista_do_tabuleiro:
            for tile in row:
                if tile.tipo != "X" and not tile.revelado:
                    return False
        return True
    
    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
        
        #Verifica exatamente onde o mouse esta sendo clicado
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= TAMANHOPISO
                my //= TAMANHOPISO

                if event.button == 1:
                    if not self.board.lista_do_tabuleiro[mx][my].bandeira:
                        #Verifica se retorna true ou false
                        if not self.board.cavar(mx, my):
                            for row in self.board.lista_do_tabuleiro:
                                for tile in row:
                                    #Se o piso for bandeira e não for bomba, mostra a imagem que voce errou
                                    if tile.bandeira and tile.tipo != "X":
                                        tile.bandeira = False
                                        tile.revelado = True
                                        tile.imagem = tile_not_mine
                                    #Se for do tipo bomba apenas revela
                                    elif tile.tipo == "X":
                                        tile.revelado = True
                            self.playing = False

                # Right Click coloca a bandeira
                if event.button == 3:
                    #Se o piso não estiver revelado ele deixa voce colocar a bandeira
                    if not self.board.lista_do_tabuleiro[mx][my].revelado:
                        #Se ja tiver a bandeira e clicar com o direito o piso volta ao normal agora se não tiver a bandeira uma é colocada
                        self.board.lista_do_tabuleiro[mx][my].bandeira = not self.board.lista_do_tabuleiro[mx][my].bandeira   

                if self.check_vitoria():
                    self.vitoria = True
                    self.playing = False
                    for row in self.board.lista_do_tabuleiro:
                        for tile in row:
                            if not tile.revelado:
                                tile.bandeira = True

    
    def end_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
        


jogo = Jogo()
while True:
    jogo.novo()
    jogo.rodar()