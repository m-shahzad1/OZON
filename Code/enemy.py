import pygame
from levelObjects import LevelObject
from gameData import enemy_size, enemies,trashBall
from projectiles import Projectile 
import math 

class Enemy(LevelObject):
    def __init__(self, screen, rect,data):

        self.data=data
        
        self.walkRight_imgs = enemies[data[2]]['sprite']['walkRight']
        self.walkLeft_imgs = enemies[data[2]]['sprite']['walkLeft']
        
        self.enemyType = data[2]

        self.walkCount = 0
        self.length = len(self.walkRight_imgs)

        # initializes enemy attributes
        self.g = 0.5
        #self.gravityon = True
        self.top_speed = enemies[data[2]]['vel']
        self.health = enemies[data[2]]['health']
        self.maxHealth = self.health
        self.prevHealth = self.health
        self.maxJump = enemies[data[2]]['maxJumpHeight']
        self.hitdamage = enemies[data[2]]['damage']

        self.look = 'right'
        # initializes enemy position 
        super().__init__(screen,rect,int(data[0]),int(data[1]),int(data[0])+int(enemy_size[0]),int(data[1])+int(enemy_size[1]),self.walkLeft_imgs[0])

        # initializes the enemy movement
        self.px1 = self.rect.left -5
        self.px2 = self.rect.right + 5
        self.top = 0

        #Projectile Parameters 
        self.projectiles = []
        self.damage = 10
        self.latency = 3000
        #projectile hits 
        self.timeCreatedfire = -5000
        self.timeCreatedice = -5000
        self.hit = False
        self.change = False
        self.damageTime = 1000
        self.timedDamage = self.health*0.1
        self.ice_speed = self.top_speed * 0.5
        ##Must PROGRAM ANGLE MECHANICS
        self.angle = 45
        self.velocity = 5
        self.projectile = trashBall
        # gravity 
        self.gravity()

    # sets the inital platform edge 
    def set_edge(self, platform, plat):
        self.px1 = platform.left
        self.px2 = platform.right
        self.top = platform.top

        for p in plat:
            if self.top == p.top:
                if math.isclose(self.px1, p.right, abs_tol = 40):
                #and p.top == self.top:
                    self.px1 = p.left
                if math.isclose(self.px2, p.left, abs_tol = 40): 
                #and p.top == self.top:
                    self.px2 = p.right

    # checks if the enemy is about to fall of the edge and turns it around 
    def check_edge(self):
        if self.rect.right >= self.px2:
            self.setVelo((-self.top_speed,0))

        elif self.rect.left <= self.px1:
            self.setVelo((self.top_speed,0))

        # for p in plat:
        #     if self.top == p.top:
        #         if math.isclose(self.px1, p.right, abs_tol = 40):
        #         #and p.top == self.top:
        #             self.px1 = p.left
        #         if math.isclose(self.px2, p.left, abs_tol = 40): 
        #         #and p.top == self.top:
        #             self.px2 = p.right

    # take damage form enemy attack 
    def player_attack(self, damage):
        self.health -= damage
    
    # apply gravity
    def gravity(self):
        self.setAcc((self.acc[0],self.g))

    # enemy walking animations 
    def enemy_annimations(self):
        if self.walkCount + 1 > self.length*2:
            self.walkCount = 0
        
        if self.velo[0] > 0:
            self.setImage(str(self.walkRight_imgs[self.walkCount // 2]))
            self.walkCount += 1
        else:
            self.setImage(str(self.walkLeft_imgs[self.walkCount // 2]))
            self.walkCount += 1
    
    #enemy projectiles 
    def shoot(self,player):
        x = player[0]
        y = player[1]
        if len(self.projectiles) == 0:
            self.projectiles.append(Projectile(self.screen,(self.rect.centerx,self.rect.centery),x,y,self.projectile))
        if len(self.projectiles) > 0:
            numberOfProjectiles = len(self.projectiles)
            currentTime = pygame.time.get_ticks()
            previousProj = self.projectiles[numberOfProjectiles-1]
            if (currentTime-previousProj.getTimeCreated()>self.latency):
                self.projectiles.append(Projectile(self.screen,(self.rect.centerx,self.rect.centery),x,y,self.projectile))

    # Remove Projectiles 
    def remove_shoot(self, p):
        self.projectiles.remove(p)

    # check projectile typw
    def got_hit(self, type):
        self.hit = True
        self.change = True
        if type == 'fireBall':
            self.timeCreatedfire = pygame.time.get_ticks()          

        elif type == 'iceBall':
            self.timeCreatedice = pygame.time.get_ticks()  
            

    # apply annimations and effcts based on projectiles 
    def speical_attack(self):
        if (pygame.time.get_ticks() - self.timeCreatedfire) < 5000:   
            self.walkRight_imgs = enemies[self.data[2]]['sprite']['walkRightFire']
            self.walkLeft_imgs = enemies[self.data[2]]['sprite']['walkLeftFire']
            if (pygame.time.get_ticks() - self.timeCreatedfire) > self.damageTime:
                self.health -= self.timedDamage
                self.damageTime += 1000

        if (pygame.time.get_ticks() - self.timeCreatedice) < 5000:   
            self.walkRight_imgs = enemies[self.data[2]]['sprite']['walkRightIce']
            self.walkLeft_imgs = enemies[self.data[2]]['sprite']['walkLeftIce']
            if self.velo == (self.top_speed,0):
                self.setVelo((self.ice_speed, 0))
            elif self.velo == (-self.top_speed,0):
                self.setVelo((-self.ice_speed, 0))
            self.top_speed = self.ice_speed
            self.latency = 10000
          
        if (pygame.time.get_ticks() - self.timeCreatedfire) > 5000 and (pygame.time.get_ticks() - self.timeCreatedice) > 5000:   
            self.walkRight_imgs = enemies[self.data[2]]['sprite']['walkRight']
            self.walkLeft_imgs = enemies[self.data[2]]['sprite']['walkLeft']
            self.top_speed = enemies[self.data[2]]['vel']
            if self.velo == (self.ice_speed,0):
                self.setVelo((self.top_speed, 0))
            elif self.velo == (-self.ice_speed,0):
                self.setVelo((-self.top_speed, 0))
            self.latency = 3000
            self.damageTime = 1000
            self.hit = False
            self.change = True

    # chnage direction of enemy based on player
    def direction(self, player):
        if player =='right':
            self.look = 'right'
            self.setImage(self.walkRight_imgs[0])
        elif player =='left':
            self.look = 'left'
            self.setImage(self.walkLeft_imgs[0])

    # health bar
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
        #projectile effects 
        if self.hit == True:
            self.speical_attack()
       
        # kills projectiles 
        if self.enemyType == 'enemyStill':
            [p.update() for p in self.projectiles]

            for p in self.projectiles:
                if p.remove() == True:
                    self.projectiles.remove(p)

        if self.change:
            if self.look == 'right':
                self.setImage(self.walkRight_imgs[0])
            elif self.look == 'left':
                self.setImage(self.walkLeft_imgs[0])
            self.change = False
        
        # enemy animations
        if self.enemyType == 'enemyMove':
            self.enemy_annimations()
            self.check_edge()

        super().update()

    def show(self):
        self.health_bar()
        if self.enemyType == 'enemyStill':
            [p.show() for p in self.projectiles]
        super().show()

    def returnData(self):
        return self.data
