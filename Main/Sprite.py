import pygame

class Werido(pygame.sprite.Sprite):
    '''动画'''
    frame_width = None

    @classmethod
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.werido_surface = target
        self.image = None
        self.werido_image = None
        self.rect = None
        self.topleft = 0, 0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 0
        self.last_time = 0
    @classmethod
    def load(self, filename, width, height, columns, pos):
        self.werido_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.frame_x, self.frame_y = pos
        self.rect = self.frame_x, self.frame_y, width, height
        self.columns = columns
        rect = self.werido_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1
    @classmethod
    def update(self, current_time, rate = 120):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time =current_time

        if self.frame != self.old_frame:
            self.frame_x = (self.frame % self.columns) * self.frame_width
            self.frame_y = (self.frame // self.columns) * self.frame_height
            rect = (self.frame_x, self.frame_y, self.frame_width, self.frame_height)
            self.image = self.werido_image.subsurface(rect)
            self.old_frame = self.frame