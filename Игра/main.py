#Создай собственный Шутер!
from random import *
from pygame import *
from time import time as timer



width = 700
height = 500
fire_play = '123.mp3'
window = display.set_mode((width, height))
display.set_caption('Space shoot')
game = True
FPS = 60
clock = time.Clock()
galaxy = transform.scale(image.load('pole.jpg'), (700, 500))
mixer.init()
mixer.music.load('farm-ambience-sfx.mp3')
mixer.music.play()
#hit = mixer.Sound('hit2.mp3')
p = 300

amount_kill = 0
amount_lose = 0

rel_time = False
num_fire = 0
a = 0
b = False
font.init()
font = font.Font(None, 30)
score_kill = font.render(f'Вы уничтожили: '+ str(amount_kill), True, (100, 100, 100))
score_lose = font.render(f'Вы упустили: '+ str(amount_lose), True, (100, 100, 100))

#font 2 = font.Font(None, 70)
win = font.render('Вы выиграли!', True, (0, 255, 0))
defeat = font.render('Вы проиграли!', True, (100, 0, 0))
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y , player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Класс игрок
class Player (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed 
        if keys[K_s]:
            self.rect.y += self.speed 
    def fire (self):
        #keys = key.get_pressed()       
        bulet = Bullet('bullet.png', self.rect.x + 20, Hero.rect.y, 20, 20 , 5)
        fire.play()
        bullets.add(bulet)


#----Создание противников------
class Enemy (GameSprite):
    direction = 'left'
    def update(self):
        self.rect.y += self.speed
        global amount_lose
        if self.rect.y >= height:
            self.rect.y = randint(10, 500)
            self.rect.x = randint(10, 600)
            amount_lose+= 1 
class Asteroid (GameSprite):
    direction = 'left'
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= height:
            self.rect.y = 0
            self.rect.x = randint(10, width-50)
                
#класс пули

Hero = Player('lapata.png', 350, 400, 30, 30, 10)
crot = Enemy('crot2.png', randint(10, 500), randint(10, 600), 30, 30, 10)

monsters = sprite.Group()
asteroids = sprite.Group()
robots = sprite.Group()
robots.add(Hero)
for i in range(5):
    crot = Enemy('crot2.png', randint(10, 690), randint(10, 490), 65, 65, 0)
    monsters.add(crot)
for i in range(2):
    asteroid = Asteroid('rock.png', randint(10, 690), randint(10, 490), 65, 65, 0)
    asteroids.add(asteroid)

finish = False
while game:  
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE and sprite.groupcollide(robots, monsters, False, True):
                #hit.play()
                crot.player_x = randint(10, 690)
                crot.player_y = randint(10, 490)
                crot = Enemy('crot2.png', randint(10, 690), randint(10, 490), 65, 65, 0)
                monsters.add(crot)
                amount_kill += 1
    if finish != True:
        window.blit(galaxy, (0, 0))        
        p -= 1
        asteroids.draw(window)
        asteroids.update()
        Hero.reset()
        Hero.update()        
        monsters.draw(window)
        monsters.update()
      

        score_kill = font.render(f'Вы уничтожили: '+ str(amount_kill), True, (255, 100, 100))
        score_lose = font.render(f'Вы упустили: '+ str(amount_lose), True, (100, 100, 100))
       
        
        
        
        window.blit(score_kill, (0, 30))
        window.blit(score_lose, (0, 50))
        if Hero.speed >= 80:
            Hero.speed = 10
  


                
        
        if sprite.groupcollide(robots, asteroids, False, False) and e.key == K_SPACE or p <= 0:
            finish = True
            window.blit(defeat, (width//2,height//2))
        if amount_kill >= 10:
            finish = True
            window.blit(win, (width//2,height//2))

        clock.tick(FPS)
        display.update()





    else:
        finish = False
        a = 0
        num_fire = 0
        amount_bullet = 0
        amount_kill = 0
        amount_lose = 0
        live = 3
        for c in asteroids:
            c.kill()
        for m in monsters:
            m.kill()
        Hero.speed = 10
        p = 300

        time.delay(3000)
        for i in range(5):
            crot = Enemy('crot2.png', randint(10, 670), randint(10, 470), 65, 65, 0)
            monsters.add(crot)
            asteroid = Asteroid('rock.png', randint(10, 670),randint(10, 470), 65, 65, 0)
            asteroids.add(asteroid)



    time.delay(50)