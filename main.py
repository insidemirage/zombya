import sys, pygame,time,math
from zombie import Zombie
from player import Player
from bullet import Bullet
swidth = 600
sheight = 600
size = width, height = swidth, sheight
black = 0,153,0
linec = 0,0,0
screen = pygame.display.set_mode(size)
player = Player(swidth, sheight)
mouse_position = (0,0)
bullets = []
while 1:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            # print(mouse_position)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            pcs = player.GetCenter()
            bullets.append(Bullet(pcs[0],pcs[1],mouse_position[0],mouse_position[1]))
            anx = pcs[0]-mouse_position[0]
            anyx = pcs[1]-mouse_position[1]
            rotation =  (math.atan2(anx, anyx)) * 180 / 3.14159265
            print(rotation)
    screen.fill(black)
    #Указатель направления пули

    linecenter = player.GetCenter()
    pygame.draw.line(screen,linec, linecenter, [mouse_position[0], mouse_position[1]], 1)

    # Создаем объект игрока и размещаем его по центру
    
    screen.blit(player.image,(player.x, player.y))
    # Зомбя
    zombie = Zombie(0,0)
    screen.blit(zombie.image,(zombie.x,zombie.y))
    # Пуля 
    for bullet in bullets:
        bullet.Move(mouse_position[0],mouse_position[1])
        pygame.draw.rect(screen, linec, (bullet.x, bullet.y, 10, 10))

    pygame.display.flip()
    
   