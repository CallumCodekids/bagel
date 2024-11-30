import pygame
import random
from Player import Player
from Enemy import Enemy
class Game:
    def __init__(self, screen_width=600, screen_height=400, fps = 60,
                 enemy_spawn_rate = 10, enemy_width = 94, enemy_height = 135,
                 win_score = 10, start_track = "MC.mp3", bagel_track = "IT COMES.mp3", boss_track = "DOOM.mp3"):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.fps = fps
        self.spawn_rate = enemy_spawn_rate
        self.score = 0
        self.score_timer = 0
        self.spawn_timer = 0
        self.enemies = []
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.win_score = win_score
        self.won = False
        self.winning_image = "winning image.png"
        self.enemy_kill_score = 10
        self.start_track = start_track
        self.bagel_track = bagel_track
        self.boss_track = boss_track
        self.track = self.start_track

    def set_up(self):
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.player = Player(self.screen_width/2 - 25,
                             self.screen_height-100, 50, 100,"player.png",
                             self.screen, 5)
        self.background_image = pygame.image.load("example.jpg")
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (self.screen_width,
                                                        self.screen_height))
        self.clock = pygame.time.Clock()
        pygame.init()
        
    def run(self):
        self.running = True
        pygame.mixer.music.load(self.track)
        pygame.mixer.music.play(loops = -1)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.score_timer = self.score_timer + 1
            if self.score_timer >= self.fps:
                self.score = self.score + len(self.enemies)
                self.score_timer = self.score_timer = 0
                print("Your score is", self.score)
            if not self.won and self.score > self.win_score:
                print("Congrats you won")
                self.won = True
                self.player = Player(self.player.x, self.player.y, self.player.width, self.player.height, self.winning_image, self.player.screen, self.player.speed)
                self.track = self.boss_track
                pygame.mixer.music.load(self.track)
                pygame.mixer.music.play(loops = -1)
            self.spawn_timer = self.spawn_timer + 1
            if self.spawn_timer > self.fps * self.spawn_rate:
                if self.track == self.start_track:
                    self.track = self.bagel_track
                    pygame.mixer.music.load(self.track)
                    pygame.mixer.music.play(loops = -1)
                self.enemies.append(Enemy(random.randint(0, self.screen_width-self.enemy_width),
                                    random.randint(0, self.screen_height-self.enemy_height),
                                    self.enemy_width,self.enemy_height,"enemy.jpg", self.screen,
                                    random.randint(-10,10),random.randint(-10,10)))
                self.spawn_timer = 0
            self.screen.blit(self.background_image, (0,0))
            self.player.move()
            self.player.display()
            player_rectangle = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
            for enemy in self.enemies:
                enemy.move()
                enemy.display()
                enemy_rectangle = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
                if enemy_rectangle.colliderect(player_rectangle):
                    if not self.won:
                        self.running = False
                    if self.won:
                        self.enemies.remove(enemy)
                        self.score += self.enemy_kill_score
            pygame.display.flip()
            self.clock.tick(self.fps)
        print("BAGEL NO!!!")
        print("Your score was", self.score)
        pygame.quit()
            