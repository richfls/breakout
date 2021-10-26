# susbrick
import pygame#imports
import random
import math

pygame.init()

class Brick:
  def __init__(self, xpos, ypos):
    self.xpos = xpos
    self.ypos = ypos
    self.alive = True
  def draw(self):
    self.color = (138 +random.randint(-10,10), 23 +random.randint(-10,10), 17 +random.randint(-10,10))
    self.color2 = (138-22, 23-12, 17-10)
    if self.alive is True:
        pygame.draw.ellipse(screen, self.color, (self.xpos, self.ypos, 100, 80))
        pygame.draw.arc(screen, self.color2, (self.xpos+10, self.ypos-16, 110, 115), (5*math.pi)/6, (7*math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.xpos+30, self.ypos-36, 110, 150), (5*math.pi)/6, (7*math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.xpos-22, self.ypos-16, 110, 115), (11*math.pi)/6, (math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.xpos-42, self.ypos-36, 110, 150), (11*math.pi)/6, (math.pi)/6, 5)
        pygame.draw.arc(screen, ((22, 100, 8)), (self.xpos+45, self.ypos-51, 110, 115), (5*math.pi)/6, (math.pi), 8)
        pygame.draw.ellipse(screen, ((0, 0, 0)), (self.xpos, self.ypos, 100, 80), 5)
  def collide(self, x, y):
    if self.alive is True:
      if math.sqrt(((self.xpos-x)**2)+((self.ypos-y)**2)) < 50+5 and math.sqrt(((x-self.xpos)**2)+((y-self.ypos)**2)) < 50+5:
        self.alive = False


screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
#variables
doExit = False
px = 300
py = 450

bx = 200
by = 200
bVx = 5
bVy = 5
#da bricks

patch=[]
patch = [Brick(random.randrange(0, 650), random.randrange(0, 250)) for i in range (100)]

while not doExit:#game loop#########################
  #I/O section................................
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      doExit = True
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    px-=5
  if keys[pygame.K_RIGHT]:
    px+=5

  #physics.....................................
  bx += bVx
  by += bVy
  #wall ball collision
  if bx < 0 or bx+20 > 700:
    bVx *= -1
  if by < 0 or by+20 > 500:
    bVy *= -1
  #bounce ball off paddle
  if by + 20 > py and bx+20 > px and bx < px+100:
    bVy *= -1

  #render section...........................
  screen.fill((0,0,0))

#draw ALL the bricks
  for Brick in patch:
      Brick.draw()
      Brick.collide(bx,by)
      
  pygame.draw.rect(screen, (random.randint(1,255),random.randint(1,255),random.randint(1,255)), (px,py, 100, 20))
  pygame.draw.circle(screen, (random.randint(1,255),random.randint(1,255),random.randint(1,255)), (bx, by), 10,10)

  pygame.display.flip()

#end game loop#########################################
pygame.quit()
