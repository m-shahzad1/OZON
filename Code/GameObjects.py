import pygame
from pathlib import Path

class GameObject(pygame.sprite.Sprite):
    def __init__(self,screen,img_rect,img_path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(Path(img_path)),(img_rect.w,img_rect.h))
        self.rect = img_rect
        self.screen = screen
        self.acc=(0,0)
        self.velo = (0,0)

    def setSize(self,size):
        self.image = pygame.transform.scale(self.image,(size.w,size.h))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().centerx

    def setImage(self, img_path):
        self.image = pygame.transform.scale(pygame.image.load(Path(img_path)),(self.rect.width,self.rect.height))

    def show(self):
        self.screen.blit(self.image,self.rect)

    def setSpeedMag(self,mag):
        self.speed = mag    
        self.velo = (self.sx,self.sy)

    def setVelo(self,velo):
        self.velo = velo

    def setAcc(self,acc):
        self.acc = acc

    def addVelo(self,v):
        self.velo = (self.velo[0]+v[0],self.velo[1]+v[1])

    def addAcc(self,a):
        self.acc = (self.acc[0]+a[0],self.acc[1]+a[1])

    def update(self):
        self.addVelo(self.acc)
        self.rect = self.rect.move(self.velo[0],self.velo[1])
