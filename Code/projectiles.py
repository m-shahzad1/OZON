import pygame,time,math
from gameData import projectiles
from gameObjects import GameObject

class Projectile(GameObject):
    def __init__(self,screen,position,mouse_x,mouse_y,data):
        #print("projectile made")        
        self.start = pygame.math.Vector2(position)
        self.end = self.start 
        self.length = screen.get_rect().h/20
        self.speed = data['velo']*screen.get_rect().h/80
        self.damage = data['damage']
        self.type = data['type']
        self.timeCreated = pygame.time.get_ticks()
        #self.all_bullets = []
        distance_x = mouse_x - position[0]
        distance_y = mouse_y - position[1]
        angle = math.atan2(distance_y, distance_x)

        self.speed_x = self.speed * math.cos(angle)
        self.speed_y = -self.speed * math.sin(angle)
        #self.all_bullets.append([position[0], position[1], speed_x, speed_y])

        self.clock = pygame.time.Clock()
        ## Type must be of type 'string' 'fireBall', 'iceBall','trashBall'
        ##self.type = type
        super().__init__(screen,pygame.Rect(position[0],position[1],self.length,self.length),data['img'])
        #print(self.rect)
            

    def getTimeCreated(self):
        return self.timeCreated
    
    def remove(self):
        if (pygame.time.get_ticks() -  self.timeCreated) > 10000:
            #print("PROJECTILE - Killed")
            return True
        return False
            

    def update(self):
        #print(self.rect)

        self.rect.centerx += self.speed_x
        self.rect.centery -= self.speed_y

        
        ##COMMENT OUT - ENEMY FAKE!!!!
        ##enemy = GameObject(self.screen,(50,50),projectiles['fireball']['img'])
        ##collision = pygame.sprite.groupcollide(self.ball,enemy,True,False)
        
        ##Collision Detection:
        ##if collision: 
            ##Add in  data for enemy's health points here!
           ## print("Enemy hit!")

        # self.show()


        ##Updating "x" and "y"
        #t += 1 
        #g = 9.81
        #self.rect.centerx = self.position[0] + self.velocity*t*(math.cos(self.angle))
        #self.rect.centery = self.position[1] + self.velocity*t*(math.sin(self.angle)-0.5*g*t^2)

        #Finding maximum distance - to kill the sprite if reached
        #self.distance = (((self.velocity)^2)*math.sin(2*self.angle))/g
        #if self.rect.centerx > self.distance:
        #    self.kill()
        
   

       
        # Make sprites, pass them on, change thier velocity based on distanc
        #Throw - logic 
        #Update Function you will show everything.