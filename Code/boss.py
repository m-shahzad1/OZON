from levelObjects import LevelObject
from gameData import bosses, trashBall
from projectiles import Projectile 
import pygame


class Boss(LevelObject):
    def __init__(self, screen, rect,data):
        
        # Holds gameData info
        self.info = bosses[int(data[2])]
        self.img = self.info['sprite']['normal']

        self.data=data
        self.health = self.info['health']
        self.maxHealth = self.health
        self.prevHealth = self.health
        self.hitdamage = self.info['damage']
        

        super().__init__(screen,rect,int(data[0]),int(data[1]),int(data[0])+int(self.info['size'][0]),int(data[1])+int(self.info['size'][1]),self.info['sprite']['normal'])

        #Projectile Parameters 
        self.projectiles = []
        self.damage = 10
        self.latency = 1000
        ##Must PROGRAM ANGLE MECHANICS
        self.angle = 45
        self.velocity = 5
        self.projectile = trashBall
        #projectile hits 
        self.timeCreatedfire = -5000
        self.timeCreatedice = -5000
        self.hit = ' '
        self.damageTime = 1000
        self.timedDamage = self.health*0.05
        self.change = True

    def shoot(self,player):
        x = player[0]
        y = player[1]
        if len(self.projectiles) == 0:
            self.projectiles.append(Projectile(self.screen,(self.rect.centerx,self.rect.centery),x,y,self.projectile))
        if len(self.projectiles) >= 1:
            numberOfProjectiles = len(self.projectiles)
            currentTime = pygame.time.get_ticks()
            previousProj = self.projectiles[numberOfProjectiles-1]
            if (currentTime-previousProj.getTimeCreated()>self.latency):
                self.projectiles.append(Projectile(self.screen,(self.rect.centerx,self.rect.centery),x,y,self.projectile))

    
    def remove_shoot(self, p):
        self.projectiles.remove(p)

    
    def player_attack(self, damage):
        self.health -= damage
    
    def got_hit(self, type):
        self.hit = True
        self.change = True
        if type == 'fireBall':
            self.timeCreatedfire = pygame.time.get_ticks()          

        elif type == 'iceBall':
            self.timeCreatedice = pygame.time.get_ticks()   

    def speical_attack(self):
        if (pygame.time.get_ticks() - self.timeCreatedfire) < 5000:   
            self.img = self.info['sprite']['fire']
            if (pygame.time.get_ticks() - self.timeCreatedfire) > self.damageTime:
                self.health -= self.timedDamage
                self.damageTime += 1000

        if (pygame.time.get_ticks() - self.timeCreatedice) < 5000:   
            self.img = self.info['sprite']['ice']
            self.latency = 6000

               
        if (pygame.time.get_ticks() - self.timeCreatedfire) > 5000 and (pygame.time.get_ticks() - self.timeCreatedice) > 5000:   
            self.img = self.info['sprite']['normal']
            self.latency = 3000
            self.damageTime = 1000
            self.hit = False
            self.change = True

    def health_bar(self):
        r = pygame.Rect(self.rect.left,self.rect.top - 15,self.rect.w,10)
        pygame.draw.rect(self.screen, (169,169,169), r)
        h = pygame.Rect(self.rect.left,self.rect.top - 15,(self.health/self.maxHealth)*self.rect.w,10)
        pygame.draw.rect(self.screen, 'green', h)

    def health_bar(self):
        r = pygame.Rect(self.rect.left,self.rect.top - 15,self.rect.w,10)
        pygame.draw.rect(self.screen, (169,169,169), r)

        r2 = pygame.Rect(self.rect.left,self.rect.top - 15,(self.health/self.maxHealth)*self.rect.w,10)
        pygame.draw.rect(self.screen, 'green', r2)

        if self.prevHealth > self.health:
            r3 = pygame.Rect(r2.right,self.rect.top - 15,((self.prevHealth-self.health)/self.maxHealth)*self.rect.w,10)
            pygame.draw.rect(self.screen, 'red', r3)

            self.prevHealth = self.health

    def update(self):
        [p.update() for p in self.projectiles]

        for p in self.projectiles:
            if p.remove() == True:
                self.projectiles.remove(p)

        #projectile effects 
        if self.hit == True:
            self.speical_attack()

        if self.change:
            self.setImage(self.img)
            self.change = False

        return super().update()  

    def show(self):
        [p.show() for p in self.projectiles]
        self.health_bar()
        super().show()

    def returnData(self):
        return self.data
