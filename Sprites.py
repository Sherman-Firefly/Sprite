import pygame
import random

pygame.init()

scce=pygame.USEREVENT +1
bcce=pygame.USEREVENT + 2

blue=pygame.Color('blue')
lblue=pygame.Color('lightblue')
dblue=pygame.Color('darkblue')

white=pygame.Color('white')
yellow=pygame.Color('yellow')
green=pygame.Color('green')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color,height,width):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        bh=False
        if self.rect.left <=0 or self.rect.right >=500:
            self.velocity[0] = -self.velocity[0]
            bh=True
        if self.rect.top <=0 or self.rect.bottom >=500:
            self.velocity[1] =- self.velocity [1]
            bh=True
        if bh:
            pygame.event.post(pygame.event.Event(scce))
            pygame.event.post(pygame.event.Event(bcce))
    
    def cc(self):
        self.image.fill(random.choice([white, yellow, green]))

def cbg():
    return random.choice([blue, lblue, dblue])

asl=pygame.sprite.Group()
st1=Sprite(white, 10, 20)
st1.rect.x=random.randint(0, 450)
st1.rect.y=random.randint(0,450)
asl.add(st1)

screen=pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

done=False
bg_color = blue
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        elif event.type== scce:
            st1.cc()
        elif event.type==bcce:
            bg_color=cbg()
    asl.update()
    screen.fill(bg_color)
    asl.draw(screen)

    clock.tick(250)


    pygame.display.flip()
pygame.quit()


