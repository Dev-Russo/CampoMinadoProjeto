from timer import *
import time
from settings import *

class DisplayTimer(pygame.sprite.Sprite):
    def __init__(self, tempo_total, fonte, cor, posicao):
        super().__init__()
        # Inicializa o temporizador com a duração total, fonte, cor e posição na tela
        self.tempo_total = tempo_total
        self.tempo_restante = tempo_total
        self.font = pygame.font.SysFont(None, fonte)  # Configura a fonte para o temporizador
        self.color = cor  # Define a cor do texto do temporizador
        self.posicao = posicao  # Define a posição onde o temporizador será desenhado
        self.start_time = time.time()  # Armazena o tempo inicial
        self.is_running = False  # Flag para verificar se o temporizador está em execução

    def start(self):
        # Inicia ou reinicia o temporizador
        self.start_time = time.time()  # Atualiza o tempo inicial
        self.tempo_restante = self.tempo_total  # Reinicia o tempo restante
        self.is_running = True  # Marca o temporizador como em execução

    def update(self):
        # Atualiza o tempo restante do temporizador
        if self.is_running:
            elapsed_time = int(time.time() - self.start_time)  # Calcula o tempo decorrido
            self.tempo_restante = max(self.tempo_total - elapsed_time, 0)  # Calcula o tempo restante
            if self.tempo_restante <= 0:
                self.tempo_restante = 0  # Garante que o tempo restante não seja negativo
                self.is_running = False  # Para o temporizador se o tempo acabou

    def draw(self, surface):
        # Desenha o temporizador na superfície fornecida
        self.update()  # Atualiza o tempo restante antes de desenhar
        timer_text = self.font.render(f"Tempo: {self.tempo_restante}s", True, self.color)  # Cria o texto do temporizador
        surface.blit(timer_text, self.posicao)  # Desenha o texto na superfície na posição especificada

    def is_time_up(self):
        # Verifica se o tempo acabou
        return self.tempo_restante <= 0

