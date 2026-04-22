from pygame import *
from pygame.sprite import *
from pygame.font import *
 
init()
fpsClock = time.Clock()
screen = display.set_mode((1000, 600))
display.set_caption('test caption')

purple = Color(128, 0, 128)

class Figure(Sprite):
    def __init__(self):
        # Sprite.init(self)
        self.image = image.load("Lecture materials\YGpOh.png").convert()
        self.image = Surface((125, 125)).convert_alpha()
        self.rect=self.image.get_rect().move(10, 10)
        # initialrect = self.image.get_rect()
        # otherrect = Rect(10, 10, 100, 50)
        # self.rect = initialrect.clip(otherrect)
        # self.image = self.image.subsurface(otherrect)
        
class Banner(Sprite):
    def __init__(self):
        my_font = Font(None, 20)
        self.image = my_font.render("Hello PyGame 123", True, (110, 10, 120))
        self.rect = self.image.get_rect().move(10, 10)
        
# class Line(Sprite):
#     def __init__(self):
#         self.image = Surface((90, 5)).convert()
#         self.rect = draw.line(screen, (128, 0, 128), (10, 10), (100, 10), 4)
        
f1 = Figure()
x= 130
# b1 = Banner()
# line = Line()
while True:
     
    # e = event.wait()
    # e = event.get(QUIT)
    k_p = key.get_pressed()           
    if k_p[K_RIGHT]:
        x +=5
    elif k_p[K_LEFT]:
        x -=5
    # elif e == QUIT:
    #     quit()              # shuts down pyGame
        # break
    

    screen.fill((255, 255, 255))   # white background
    f1.image.fill((128, 0, 128, 128))
    # screen.blit(line.image, (10, 10))
    screen.blit(f1.image, (x, 210))
    x += 2
    # draw.circle(screen, purple, (30, 40), 20, 2)
    # draw.rect(screen, purple, Rect(10, 10, 80, 100), 3)
    draw.polygon(screen, purple, ((30, 100), (110, 100), (25, 60), (200, 200), (85, 120)), 0)

    
    # screen.blit(b1.image, (20, 20))
    display.flip() 
    fpsClock.tick(10)              