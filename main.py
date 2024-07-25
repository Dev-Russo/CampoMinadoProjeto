import pygame
from settings import *
from sprites import *
from displaytimer import *

pygame.init()

class Jogo:
    def __init__(self):
        # Configura a tela do jogo e o título da janela
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO)
        # Configura o relógio para controlar o FPS
        self.clock = pygame.time.Clock()
        # Cria e configura o temporizador
        self.timer = DisplayTimer(TEMPO_TOTAL, FONTE_TAMANHO, FONTE_COR, TIMER_POSICAO)
        # Flag para indicar se o jogo terminou
        self.jogo_terminado = False

    def novo(self):
        # Inicializa um novo tabuleiro e reinicia o temporizador
        self.board = Tabuleiro()
        self.board.mostrar_tabuleiro()
        self.timer.start()
        self.jogo_terminado = False

    def rodar(self):
        # Inicializa um novo jogo e começa o loop principal
        self.novo()
        while True:
            self.clock.tick(FPS)  # Controla a taxa de atualização da tela
            self.eventos()  # Processa eventos do jogo
            self.desenhar()  # Desenha o tabuleiro e o temporizador

            if not self.jogo_terminado:
                if self.timer.is_time_up():
                    # Se o tempo acabou, termina o jogo e revela todas as minas
                    self.jogo_terminado = True
                    self.revelar_todos_os_pisos()
                    self.end_screen("Tempo Acabou!")

                elif self.check_vitoria():
                    # Se o jogador venceu, termina o jogo e revela todas as minas
                    self.jogo_terminado = True
                    self.revelar_todos_os_pisos()
                    self.end_screen("Você Venceu!")

    def desenhar(self):
        # Preenche a tela com a cor de fundo
        self.screen.fill(BGCOLOR)
        # Desenha o tabuleiro na tela
        self.board.desenha(self.screen)
        # Desenha o temporizador na tela
        self.timer.draw(self.screen)
        pygame.display.flip()  # Atualiza a tela

    def check_vitoria(self):
        # Verifica se todos os pisos que não são minas foram revelados
        for row in self.board.get_lista_do_tabuleiro:
            for tile in row:
                if tile.get_tipo != "X" and not tile.get_revelado:
                    return False
        return True

    def eventos(self):
        # Processa eventos como cliques do mouse e o fechamento da janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.jogo_terminado:
                    # Se o jogo acabou e o usuário clica, inicia um novo jogo
                    self.novo()
                else:
                    # Obtém a posição do clique do mouse
                    mx, my = pygame.mouse.get_pos()
                    # Converte a posição para coordenadas do tabuleiro
                    mx //= TAMANHOPISO
                    my //= TAMANHOPISO

                    if event.button == 1:  # Clique com o botão esquerdo do mouse
                        if not self.board.get_lista_do_tabuleiro[mx][my].get_bandeira:
                            # Se o piso não tem bandeira e não é uma mina
                            if not self.board.cavar(mx, my):
                                # Se o piso cavado é uma mina, termina o jogo
                                self.jogo_terminado = True
                                self.revelar_todos_os_pisos()
                                self.end_screen("Você Perdeu!")

                    if event.button == 3:  # Clique com o botão direito do mouse
                        if not self.board.get_lista_do_tabuleiro[mx][my].get_revelado:
                            # Alterna a bandeira no piso clicado
                            self.board.get_lista_do_tabuleiro[mx][my].set_bandeira = not self.board.get_lista_do_tabuleiro[mx][my].get_bandeira

    def revelar_todos_os_pisos(self):
        # Revela todos os pisos do tabuleiro
        for row in self.board.get_lista_do_tabuleiro:
            for tile in row:
                tile.set_revelado = True
                # Define a imagem do piso conforme o tipo
                if tile.get_tipo == "X":
                    tile.set_imagem = tile_mine
                elif tile.get_tipo == "C":
                    total_minas = self.board.vizinhos(tile.get_x // TAMANHOPISO, tile.get_y // TAMANHOPISO)
                    tile.set_imagem = tile_numbers[total_minas - 1]
                else:
                    tile.set_imagem = tile_empty

    def end_screen(self, mensagem):
        # Exibe a tela final com a mensagem e aguarda o clique do mouse para reiniciar
        while True:
            self.screen.fill(BGCOLOR)
            font = pygame.font.SysFont(None, 55)
            texto = font.render(mensagem, True, BRANCO)
            texto_rect = texto.get_rect(center=(LARGURA // 2, ALTURA // 2))
            self.screen.blit(texto, texto_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

jogo = Jogo()
while True:
    jogo.novo()  # Inicializa um novo jogo
    jogo.rodar()  # Começa o loop principal do jogo
