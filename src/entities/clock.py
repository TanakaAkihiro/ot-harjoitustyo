import pygame


class Clock:
    '''
    Luokka, joka käsittelee palikoiden liikkumisen nopeutta.
    '''

    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        '''
        Liikuttaa kelloa eteenpäin.
        '''
        self._clock.tick(fps)
