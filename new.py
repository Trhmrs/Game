import pygame

class Hero:
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load('Animatronic.gif')
        self.rect=self.image.get_rect()
        self.rect.centerx=300
        self.rect.bottom=300
        self.orientation='right'
        self.orientation='left'
        self.orientation='up'
        self.orientation='down'
        self.speed=1
        self.move=False
    def blitme(self):
        if self.move:
            if self.orientation=='right':
                self.rect.centerx+=self.speed
            elif self.orientation=='left':
                self.rect.centerx-=self.speed
            elif self.orientation=='up':
                self.rect.centery-=self.speed
            elif self.orientation=='down':
                self.rect.centery+=self.speed
        self.screen.blit(self.image,self.rect)
class Hero2:
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load('purple.gif')
        self.rect=self.image.get_rect()
        self.rect.centerx=100
        self.bottom=100