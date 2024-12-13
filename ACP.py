import pygame

pygame.init()

white = (255, 255, 255)
blue = (0, 125, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Movable Rectangle")

font = pygame.font.Font(None, 36) 
text = font.render("Hello, Pygame", True, (0, 0, 0))  
text_rect = text.get_rect(center=(500 // 2, 30))

rect_width, rect_height = 60, 60
rect_x = (500 - rect_width) // 2  
rect_y = (500 - rect_height) // 2  

class MovableSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 100  
        self.rect.y = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

movable_sprite = MovableSprite(red, 50, 50)
all_sprites = pygame.sprite.Group()
all_sprites.add(movable_sprite)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites.update()

    display_surface.fill(white)

    display_surface.blit(text, text_rect)

    pygame.draw.rect(display_surface, blue, pygame.Rect(rect_x, rect_y, rect_width, rect_height))

    all_sprites.draw(display_surface)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
