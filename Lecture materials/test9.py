from pygame import *
from pygame.sprite import *
from pygame.font import *

init()
screen = display.set_mode((300, 450))
display.set_caption('test caption')


class Figure(Sprite):
    def __init__(self):
        # Sprite.init(self)
        self.image = image.load("Lecture materials\YGpOh.png").convert()
        initialrect = self.image.get_rect()
        otherrect = Rect(10, 10, 100, 50)
        self.rect = initialrect.clip(otherrect)
        self.image = self.image.subsurface(otherrect)
        
class Banner(Sprite):
    def __init__(self):
        my_font = Font(None, 20)
        self.image = my_font.render("Hello PyGame 123", True, (110, 10, 120))
        self.rect = self.image.get_rect().move(10, 10)
        
f1 = Figure()
b1 = Banner()
while True:
     
    e = event.wait()           
    if e.type == QUIT:
        quit()              # shuts down pyGame
        break

    screen.fill((255, 255, 255))   # white background
    screen.blit(f1.image, (130, 210))
    screen.blit(b1.image, (20, 20))
    display.update()               