import pygame

class Timer:
    def __init__(self, duration):
        self._duration = duration
        self._start_time = None

    def start(self):
        self._start_time = pygame.time.get_ticks()

    def get_elapsed_time(self):
        if self._start_time is None:
            return 0
        return (pygame.time.get_ticks() - self._start_time) / 1000

    def get_remaining_time(self):
        return max(self._duration - self.get_elapsed_time(), 0)

    def is_time_up(self):
        return self.get_remaining_time() <= 0

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def get_start_time(self):
        return self._start_time

    def set_start_time(self, start_time):
        self._start_time = start_time
