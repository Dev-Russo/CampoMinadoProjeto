from timer import *
import time
from settings import *
import pygame

class DisplayTimer(Timer):
    def __init__(self, duration, font_size, color, position):
        super().__init__(duration)
        self._font = pygame.font.SysFont(None, font_size)
        self._color = color
        self._position = position
        self._is_running = False

    def start(self):
        super().start()
        self._is_running = True

    def update(self):
        if self._is_running:
            if self.is_time_up():
                self._is_running = False

    def draw(self, surface):
        self.update()
        remaining_time = self.get_remaining_time()
        timer_text = self._font.render(f"Tempo: {int(remaining_time)}s", True, self._color)
        surface.blit(timer_text, self._position)

    def is_time_up(self):
        return super().is_time_up()


    