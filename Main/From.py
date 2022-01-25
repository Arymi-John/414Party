import random
import Sprite
from Sprite import Werido
import pygame
import sys




class Player(pygame.sprite.Sprite):
    '''定义角色类'''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_x = 200
        self.player_y = 400
        self.staue = 1
        self.frame = 0
        self.rect = None
        self.image = None
        self.player_img = None
        self.old_frame = -1
        self.topleft = 0, 0
        self.frame_width = 1
        self.frame_height = 1
        self.last_frame = 0
        self.first_frame = 0
        self.last_time = 0
        self.columns = 0
        self.player_surface = screen

    def load(self):
        self.player_img = [pygame.image.load("../Images/stand.png"),
                           pygame.image.load("../Images/四海front.png").convert_alpha(),
                           pygame.image.load("../Images/四海right.png").convert_alpha()]
        self.frame_width = 100
        self.frame_height = 100
        self.rect = 100, 100, 100, 100
        self.columns = 3
        rect = self.player_img[self.staue].get_rect()
        self.last_frame = (rect.width // 100) * (rect.height // 100) - 1

    def update(self, current_time, rate = 60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            self.frame_x = (self.frame % self.columns) * self.frame_width
            self.frame_y = (self.frame // self.columns) * self.frame_height
            rect = (self.frame_x, self.frame_y, self.frame_width, self.frame_height)
            self.image = self.player_img[self.staue].subsurface(rect)
            self.old_frame = self.frame
        self.keylist = pygame.key.get_pressed()
        if self.keylist[pygame.K_s]:
            self.staue = 1

        if self.keylist[pygame.K_d]:
            self.staue = 2



#     def __init__(self):
#         self.player_x = 400
#         self.player_y = 200
#         self.Player_HP = 100
#         self.Player_MP = 100
#     def create(self):
#         self.player = Werido(screen)
#         group.add(self.player)
#         self.devil_num = 0
#         self.devil_img = pygame.image.load('../Images/四海.png')
#         pygame.draw.rect(screen, color='red', rect=((50, 30), (self.Player_HP * 2, 20)), width=0)
#         pygame.draw.rect(screen, color='blue', rect=((50, 60), (self.Player_MP * 2, 20)), width=0)
#         Text_HP = font.render('HP', True, ('#ffffff'), None)
#         Text_MP = font.render('MP', True, ('#ffffff'), None)
#         screen.blit(Text_HP, (20, 30))
#         screen.blit(Text_MP, (20, 60))
#
#     def update(self):
#         Werido.load("../Images/ 四海.png", 100, 100, 3, (self.player_x, self.player_y))


def CreateMap():
    screen.fill((0, 0, 0))
    mapstatue = [pygame.image.load('../Images/map000.png')]
    mapnum = 0
    map = pygame.transform.scale(mapstatue[mapnum], resloving[0])
    screen.blit(map, (0, 0))
    screen.blit(logo, logo.get_rect(center=old_core))
    setup = pygame.image.load('../Images/设置.png').convert_alpha()
    setup = pygame.transform.scale(setup, (20, 20))
    screen.blit(setup, (width - 420, 0))


class Set(object):
    def Click_setup(self):
        mouse_pos = []
        for event in pygame.event.get():
            keylist = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos.append(event.pos)
                mouse_x, mouse_y = event.pos
                if (mouse_x <= width-380 and mouse_x >= width-430) and (mouse_y >= 0 and mouse_y<= 60):
                    Set.Setup()
            if keylist[pygame.K_ESCAPE]:
                Set.Setup()
    def Setup(self):
        self.flag = False
        self.Setup_font = pygame.font.SysFont('arial', 100)
        self.content_font = pygame.font.SysFont(None, 50)
        while True:
            self.suspend_image = pygame.image.load('../Images/suspend.png')
            self.suspend_image = pygame.transform.scale(self.suspend_image, (100, 100))
            self.suspend_text = self.Setup_font.render('Pause', True, ('#ffffff'), None)
            self.continue_text = self.content_font.render('continue', True, ('#ffffff'), None)
            self.quit_text = self.content_font.render('quit', True, ('#ffffff'), None)
            screen.blit(self.suspend_image, (650, 70))
            screen.blit(self.suspend_text, (580, 210))
            screen.blit(self.continue_text, (610, 360))
            screen.blit(self.quit_text, (650, 420))
            mouse_pos = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos.append(event.pos)
                    mouse_x, mouse_y = event.pos
                    if (mouse_x >= 610 and mouse_x <= 760) and (mouse_y >= 360 and mouse_y <= 410):
                        pygame.draw.rect(screen, 'Blue', ((610, 360), (150, 40)), width=1)
                    elif (mouse_x >= 610 and mouse_x <= 760) and (mouse_y >= 420 and mouse_y <= 470):
                        pygame.draw.rect(screen, 'Blue', ((610, 420), (150, 40)), width=1)
                    else:
                        pygame.draw.rect(screen, '#5a2323', ((610, 360), (150, 40)), width=1)
                        pygame.draw.rect(screen, '#5a2323', ((610, 420), (150, 40)), width=1)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos.append(event.pos)
                    mouse_x, mouse_y = event.pos
                    if (mouse_x >= 650 and mouse_x <= 725) and (mouse_y >= 360 and mouse_y <= 410):
                        self.flag = True
                    elif (mouse_x >= 610 and mouse_x <= 760) and (mouse_y >= 420 and mouse_y <= 470):
                        sys.exit()
            if self.flag:
                break
            clock.tick(30)
            pygame.display.update()

class devil(object):
    def __init__(self):
        self.devil_x = 600
        self.devil_y = 200
        self.move_x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1300, 1400]
        self.move_y = [100, 150, 200, 250, 300, 350, 400, 450]
        self.angle = 0
        self.atklogic = 0
        self.flag = 0

    def create(self):
        self.devil = Werido(screen)
        group.add(self.devil)

    def update(self, time):
        Werido.load("../Images/devil_atk.png", 100, 100, 3, (self.devil_x, self.devil_y))
        if time % 60 == 0:
            self.movex = random.randint(0, 12)
            self.movey = random.randint(0, 7)
            self.devil_x = self.move_x[self.movex]
            self.devil_y = self.move_y[self.movey]
            self.atklodic = 1
        if self.atklogic == 0:
            devil.attack()

    def attack(self):
        self.speed = 10
        if self.flag == 0:
            self.attack_x = self.devil_x + 75
            self.attack_y = self.devil_y + 72
            self.angle += 5
            self.image = pygame.image.load("../Images/bo1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (20, 20))
            self.image = pygame.transform.rotate(self.image, self.angle)
            screen.blit(self.image, (self.attack_x, self.attack_y))
            self.soud = pygame.mixer.Sound("../Studio/atk00.wav")
            self.soud.play(0)
            self.flag = 1
        else:
            if self.attack_x <= 1920 and self.attack_x >= 0:
                self.attack_x += self.speed
            screen.blit(self.image, (self.attack_x, self.attack_y))
            if self.attack_x > 1920:
                self.flag = 0




if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load('D:/Project/414Party/Studio/414bgm.wav')
    pygame.mixer.music.play(-1)
    pygame.display.set_icon(pygame.image.load("../Images/logo.png"))
    font = pygame.font.SysFont(None, 30)
    resloving = pygame.display.list_modes()
    width, height = resloving[0]
    print(resloving)
    screen = pygame.display.set_mode(resloving[0], flags=pygame.DOUBLEBUF | pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    logo = pygame.image.load('../Images/logo.png')
    old_core = logo.get_rect().center
    angle = 0
    Set = Set()
    devil = devil()
    player = Player()
    group = pygame.sprite.Group()
    groups = pygame.sprite.Group()
    devil.create()
    groups.add(player)
    player.load()

    while True:

        clock.tick(30)
        ticks = pygame.time.get_ticks()
        mouse_pos = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        logo = pygame.image.load('../Images/logo.png')
        logo = pygame.transform.scale(logo, (100, 100))
        old_core = logo.get_rect().center
        logo = pygame.transform.rotate(logo, angle)
        CreateMap()
        angle += 1

        devil.update(ticks)
        # if keylist[pygame.K_Space]:
        #     Setup.fundation()
        Set.Click_setup()
        group.update(ticks)
        group.draw(screen)
        groups.update(ticks)
        groups.draw(screen)
        pygame.display.flip()