# Abstergo LLC | Colin Jackson | 10-30-2022

import pygame
from datetime import datetime

def getKeyPress():

    while True:
        
        pygame.display.update()
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            print("A key has been pressed: {}".format(pygame.key.name(event.key)))
            return event.key
        else:
            pass


def main():

    pygame.init()
    pygame.display.set_mode((128, 128), 0, 32)
    startTime = datetime.now()

    print("Start time: {}".format(startTime))

    # runs the getKeyPress function which prints the key pressed
    while True:
        getKeyPress()

main()
