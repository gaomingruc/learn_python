# Example file showing a basic pygame "game loop"
import random
import time
import pygame


class Block(pygame.sprite.Sprite):
    blocks_number = 0
    infected_number = 0

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(
            (random.randint(10, 30), random.randint(10, 30)))
        self.color = "black"
        self.image.fill(self.color)
        self.rect = self.image.get_rect(
            center=(random.randint(0, 800), random.randint(0, 800)))
        self.infected_timestamp = 0

    def change_color(self):
        self.image.fill("red")
        self.color = "red"
        self.infected_timestamp = pygame.time.get_ticks()

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
                if item.color == "black":
                    item.change_color()

    def die(self):
        if (self.color == "red") and (pygame.time.get_ticks() - self.infected_timestamp > 5000):
            self.kill()

    @staticmethod
    def born():
        block_group.add(Block())

    def update(self):
        self.random_walk()
        self.infect()
        self.die()
        Block.get_infected_number()
        Block.get_blocks_number()

    @classmethod
    def get_infected_number(cls):
        cls.infected_number = 0
        for block in block_group:
            if block.color == "red":
                cls.infected_number += 1

    @classmethod
    def get_blocks_number(cls):
        cls.blocks_number = len(block_group)


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


class Score(object):
    def __init__(self):
        self.blocks_number = 0
        self.infected_number = 0
        self.time = 0
        self.font = pygame.font.Font("font/Pixeltype.ttf", 50)

    def show(self):
        self.show_title()
        self.show_infected_number()
        self.show_time()
        self.show_blocks_number()

    def show_title(self):
        self.surface = self.font.render("epidemic simulator by Gao Ming", False, (64, 64, 64))
        self.rect = self.surface.get_rect(topleft=(0, 0))
        screen.blit(self.surface, self.rect)

    def show_infected_number(self):
        self.surface = self.font.render(
            "infected: %s" % self.infected_number, False, (64, 64, 64))
        self.rect = self.surface.get_rect(center=(700, 60))
        screen.blit(self.surface, self.rect)

    def show_time(self):
        self.surface = self.font.render(
            "time: %.2f" % (self.time / 1000), False, (64, 64, 64))
        self.rect = self.surface.get_rect(center=(700, 100))
        screen.blit(self.surface, self.rect)

    def show_blocks_number(self):
        self.surface = self.font.render(
            "blocks: %s" % self.blocks_number, False, (64, 64, 64))
        self.rect = self.surface.get_rect(center=(700, 20))
        screen.blit(self.surface, self.rect)

    def update(self):
        self.infected_number = Block.infected_number
        self.time = pygame.time.get_ticks()
        self.blocks_number = Block.blocks_number


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

# score
score = Score()

# Timer
born_timer = pygame.USEREVENT + 1
pygame.time.set_timer(born_timer, 1000)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == born_timer:
            Block.born()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE
    block_group.update()
    block_group.draw(screen)

    hero_group.update()
    hero_group.draw(screen)

    score.update()
    score.show()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
