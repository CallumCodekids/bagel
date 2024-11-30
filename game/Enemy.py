import pygame

class Enemy:
    
    def __init__(self, x, y, width, height, image, screen, x_speed, y_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.screen = screen
        self.x_speed = x_speed
        self.y_speed = y_speed
        
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        
    def move(self):
        old_x = self.x
        old_y = self.y
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        player_rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        screen_rectangle = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        screen_contains_player = screen_rectangle.contains(player_rectangle)
        if not screen_contains_player:
            if self.x +self.width > self.screen.get_width() or self.x < 0:
                self.x_speed = self.x_speed * -1
            if self.y +self.height > self.screen.get_height() or self.y < 0:
                self.y_speed = self.y_speed * -1
            self.x = old_x
            self.y = old_y
        
        