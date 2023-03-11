from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
back = (150, 255, 10)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
 
run = True
finish = False
clock = time.Clock()
FPS = 60

racket_1 = Player('racket.png', 30, 200, 4, 50, 150)
racket_2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 255, 230, 10, 50, 50)
 
speed_x = -3
speed_y = -3 

while run:
    for e in event.get():
        if e.type == QUIT:
           run = False
    window.fill(back)
    racket_1.update_l()
    racket_2.update_r()

    ball.reset()
    racket_1.reset()
    racket_2.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
        speed_x *= -1
        speed_y *= 1
    display.update()
    clock.tick(FPS)
