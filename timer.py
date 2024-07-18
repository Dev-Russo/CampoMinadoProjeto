import pygame

class Timer:
    def __init__(self, duration):
        # Inicializa o temporizador com a duração especificada
        self._duration = duration  # Duração total do temporizador em segundos
        self._start_time = None  # Armazena o tempo de início do temporizador

    def start(self):
        # Inicia ou reinicia o temporizador
        self._start_time = pygame.time.get_ticks()  # Captura o tempo atual em milissegundos

    def get_elapsed_time(self):
        # Calcula o tempo decorrido desde o início do temporizador
        if self._start_time is None:
            return 0  # Se o temporizador não foi iniciado, o tempo decorrido é 0
        return (pygame.time.get_ticks() - self._start_time) / 1000  # Calcula o tempo decorrido em segundos

    def get_remaining_time(self):
        # Calcula o tempo restante do temporizador
        return max(self._duration - self.get_elapsed_time(), 0)  # Garante que o tempo restante não seja negativo

    def is_time_up(self):
        # Verifica se o tempo do temporizador acabou
        return self.get_remaining_time() <= 0  # Retorna True se o tempo restante for 0 ou negativo

    def get_duration(self):
        # Retorna a duração total do temporizador
        return self._duration

    def set_duration(self, duration):
        # Define uma nova duração para o temporizador
        self._duration = duration

    def get_start_time(self):
        # Retorna o tempo de início do temporizador
        return self._start_time

    def set_start_time(self, start_time):
        # Define um novo tempo de início para o temporizador
        self._start_time = start_time
