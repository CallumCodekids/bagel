import pygame

class Player:
    
    def __init__(self, x, y, width, height, image, screen, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.screen = screen
        self.speed = speed
        
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        
    def move(self):
        old_x = self.x
        old_y = self.y
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            self.y = self.y - self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.y = self.y + self.speed
        if keys_pressed[pygame.K_LEFT]:
            self.x = self.x - self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.x = self.x + self.speed
        player_rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        screen_rectangle = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        screen_contains_player = screen_rectangle.contains(player_rectangle)
        if not screen_contains_player:
            self.x = old_x
            self.y = old_y