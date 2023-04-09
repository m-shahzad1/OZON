"""
import pygame


class Music{

    def __init__(self,level):
        self.level = level

    def startMusic1(self,level):
    
        #Level 1,2
        pygame.mixer.music.load('Code\Assets\backgroundMusic\\bgm3.mp3')


    def startMusic3():
    ##Level 6,7
        pygame.mixer.music.load('Code\Assets\backgroundMusic\\bgm2.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1,fade_ms=3000)

    def startMusic4():
    #Ending Sequence and beyond 
        pygame.mixer.music.load('Code\Assets\backgroundMusic\\bgm4.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1,fade_ms=3000)

    def pauseMusic():
        pygame.mixer.music.pause()

    def playMusic():
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1,fade_ms=3000)

    


}
"""