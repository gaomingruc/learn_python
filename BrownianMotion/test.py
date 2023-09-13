# Example file showing a basic pygame "game loop"
import random
import time
import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(
            (random.randint(10, 30), random.randint(10, 30)))
        self.color = "black"
        self.image.fill(self.color)
        self.rect = self.image.get_rect(
            center=(random.randint(0, 800), random.randint(0, 800)))

    def change_color(self):
        self.image.fill("red")
        self.color = "red"

    def random_walk(self):
        if (self.rect.centerx > 0) and (self.rect.centerx < 800) and (self.rect.centery > 0) and (self.rect.centery < 800):
            self.rect.centerx += random.randint(-10, 10)
            self.rect.centery += random.randint(-10, 10)
        elif self.rect.centerx <= 0:
            self.rect.centerx += 10
        elif self.rect.centerx >= 800:
            self.rect.centerx -= 10
        elif self.rect.centery <= 0:
            self.rect.centery += 10
        elif self.rect.centery >= 800:
            self.rect.centery -= 10

    def infect(self):
        if self.color == "red" and pygame.sprite.spritecollide(self, block_group, False):
            for item in pygame.sprite.spritecollide(self, block_group, False):
                item.change_color()

    def die(self):
        if self.color == "red":
            self.kill()

    def update(self):
        self.random_walk()
        self.infect()


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = "red"
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(0, 0))

    def move(self):
        # 得到玩家键盘输入
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.centerx -= 10
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.centerx += 10
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.centery -= 10
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.centery += 10

    def check_collide(self):
        if pygame.sprite.spritecollide(self, block_group, False):
            block = pygame.sprite.spritecollide(self, block_group, False)[0]
            block.change_color()

    def update(self):
        self.move()
        self.check_collide()


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

# block组
block_list = [Block() for i in range(100)]
block_group = pygame.sprite.Group()
block_group.add(block_list)

# hero
hero = Hero()
hero_group = pygame.sprite.GroupSingle()
hero_group.add(hero)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE
    block_group.update()
    block_group.draw(screen)

    hero_group.update()
    hero_group.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
