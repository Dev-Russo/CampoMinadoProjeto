from timer import *
import time
from settings import *
import pygame

class DisplayTimer(pygame.sprite.Sprite):
    def __init__(self, tempo_total, fonte, cor, posicao):
        super().__init__()
        # Inicializa o temporizador com a duração total, fonte, cor e posição na tela
        self._tempo_total = tempo_total
        self._tempo_restante = tempo_total
        self._font = pygame.font.SysFont(None, fonte)  # Configura a fonte para o temporizador
        self._color = cor  # Define a cor do texto do temporizador
        self._posicao = posicao  # Define a posição onde o temporizador será desenhado
        self._start_time = time.time()  # Armazena o tempo inicial
        self._is_running = False  # Flag para verificar se o temporizador está em execução


    # Métodos Getters e Setters
    def get_tempo_total(self):
        return self._tempo_total

  
    def set_tempo_total(self, value):
        self._tempo_total = value

    
    def get_tempo_restante(self):
        return self._tempo_restante

    
    def set_tempo_restante(self, value):
        self._tempo_restante = value

    
    def get_font(self):
        return self._font

    
    def set_font(self, value):
        self._font = value

   
    def get_color(self):
        return self._color

    
    def set_color(self, value):
        self._color = value

    
    def get_posicao(self):
        return self._posicao

   
    def set_posicao(self, value):
        self._posicao = value

    
    def get_start_time(self):
        return self._start_time

    
    def set_start_time(self, value):
        self._start_time = value

    
    def get_is_running(self):
        return self._is_running

    
    def set_is_running(self, value):
        self._is_running = value


    def start(self):
        # Inicia ou reinicia o temporizador
        self._start_time = time.time()  # Atualiza o tempo inicial
        self._tempo_restante = self._tempo_total  # Reinicia o tempo restante
        self._is_running = True  # Marca o temporizador como em execução

    def update(self):
        # Atualiza o tempo restante do temporizador
        if self._is_running:
            elapsed_time = int(time.time() - self._start_time)  # Calcula o tempo decorrido
            self._tempo_restante = max(self._tempo_total - elapsed_time, 0)  # Calcula o tempo restante
            if self._tempo_restante <= 0:
                self._tempo_restante = 0  # Garante que o tempo restante não seja negativo
                self._is_running = False  # Para o temporizador se o tempo acabou

    def draw(self, surface):
        # Desenha o temporizador na superfície fornecida
        self.update()  # Atualiza o tempo restante antes de desenhar
        timer_text = self._font.render(f"Tempo: {self._tempo_restante}s", True, self._color)  # Cria o texto do temporizador
        surface.blit(timer_text, self._posicao)  # Desenha o texto na superfície na posição especificada

    def is_time_up(self):
        # Verifica se o tempo acabou
        return self._tempo_restante <= 0

    