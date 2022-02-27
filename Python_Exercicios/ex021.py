#import pygame
#pygame.init()
#pygame.mixer.music.load('aud21.mp3')
#pygame.mixer.music.play(loops=0, start=0.0)
#pygame.event.wait()
#Não funciona!!!!!

#Outras que funcionam
#from playsound import playsound
#playsound("ex021.mp3")

import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
